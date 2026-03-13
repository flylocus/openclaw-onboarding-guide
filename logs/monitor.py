#!/usr/bin/env python3
"""
openclaw-onboarding-guide 监控脚本 v1
轻量级数据统计工具 - Phase A MVP
"""

import json
from datetime import datetime, timedelta
from collections import Counter
from pathlib import Path
import argparse

LOGS_DIR = Path(__file__).parent

def load_logs(date_str):
    """读取指定日期的日志"""
    log_path = LOGS_DIR / f"triggers_{date_str}.jsonl"
    if not log_path.exists():
        return []
    
    logs = []
    with open(log_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    logs.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
    return logs

def generate_daily_report(date_str, logs):
    """生成日报"""
    if not logs:
        return f"## {date_str} 汇总\n\n无数据\n"
    
    total = len(logs)
    triggered = sum(1 for l in logs if l.get('triggered', False))
    false_pos = sum(1 for l in logs if l.get('false_positive', False))
    
    # 路由层级统计
    layer_counts = Counter(l.get('routed_layer') for l in logs if l.get('routed_layer'))
    
    # 问题级别统计
    issue_counts = Counter(l.get('issue_level') for l in logs if l.get('issue_level'))
    
    # 用户接受度
    accepted = sum(1 for l in logs if l.get('user_accepted', False))
    clear_step = sum(1 for l in logs if l.get('clear_next_step', False))
    
    # 计算比率
    trigger_rate = (triggered / total * 100) if total > 0 else 0
    accept_rate = (accepted / triggered * 100) if triggered > 0 else 0
    false_rate = (false_pos / triggered * 100) if triggered > 0 else 0
    
    report = f"""## {date_str} 汇总

### 核心指标

| 指标 | 数值 |
|------|------|
| 总 query 数 | {total} |
| 触发次数 | {triggered} |
| 触发率 | {trigger_rate:.1f}% |
| 误触发 | {false_pos} |
| 误触发率 | {false_rate:.1f}% |
| 用户接受 | {accepted} |
| 接受率 | {accept_rate:.1f}% |
| 知道下一步 | {clear_step} |

### 路由层级分布

| 层级 | 次数 |
|------|------|
| L1 | {layer_counts.get('L1', 0)} |
| L2 | {layer_counts.get('L2', 0)} |
| L3 | {layer_counts.get('L3', 0)} |
| L4 | {layer_counts.get('L4', 0)} |
| L5 | {layer_counts.get('L5', 0)} |

### 问题统计

| 级别 | 数量 |
|------|------|
| P0 | {issue_counts.get('P0', 0)} |
| P1 | {issue_counts.get('P1', 0)} |
| P2 | {issue_counts.get('P2', 0)} |

### Top Query

"""
    # Top 5 query
    query_counts = Counter(l.get('query', '') for l in logs if l.get('triggered', False))
    for i, (query, count) in enumerate(query_counts.most_common(5), 1):
        report += f"{i}. `{query}` ({count}次)\n"
    
    return report

def generate_weekly_report(week_start, days=7):
    """生成周报"""
    all_logs = []
    dates = []
    
    for i in range(days):
        date = (week_start + timedelta(days=i)).strftime('%Y-%m-%d')
        dates.append(date)
        logs = load_logs(date)
        all_logs.extend(logs)
    
    if not all_logs:
        return f"## Week of {week_start.strftime('%Y-%m-%d')} 汇总\n\n无数据\n"
    
    total = len(all_logs)
    triggered = sum(1 for l in all_logs if l.get('triggered', False))
    false_pos = sum(1 for l in all_logs if l.get('false_positive', False))
    accepted = sum(1 for l in all_logs if l.get('user_accepted', False))
    
    layer_counts = Counter(l.get('routed_layer') for l in all_logs if l.get('routed_layer'))
    issue_counts = Counter(l.get('issue_level') for l in all_logs if l.get('issue_level'))
    query_counts = Counter(l.get('query', '') for l in all_logs if l.get('triggered', False))
    
    trigger_rate = (triggered / total * 100) if total > 0 else 0
    accept_rate = (accepted / triggered * 100) if triggered > 0 else 0
    false_rate = (false_pos / triggered * 100) if triggered > 0 else 0
    
    report = f"""## Week of {week_start.strftime('%Y-%m-%d')} 汇总

### 周核心指标

| 指标 | 数值 |
|------|------|
| 总 query 数 | {total} |
| 触发次数 | {triggered} |
| 触发率 | {trigger_rate:.1f}% |
| 误触发 | {false_pos} |
| 误触发率 | {false_rate:.1f}% |
| 用户接受 | {accepted} |
| 接受率 | {accept_rate:.1f}% |

### 路由层级分布

| 层级 | 次数 | 占比 |
|------|------|------|
| L1 | {layer_counts.get('L1', 0)} | {layer_counts.get('L1', 0)/triggered*100:.1f}% |
| L2 | {layer_counts.get('L2', 0)} | {layer_counts.get('L2', 0)/triggered*100:.1f}% |
| L3 | {layer_counts.get('L3', 0)} | {layer_counts.get('L3', 0)/triggered*100:.1f}% |
| L4 | {layer_counts.get('L4', 0)} | {layer_counts.get('L4', 0)/triggered*100:.1f}% |
| L5 | {layer_counts.get('L5', 0)} | {layer_counts.get('L5', 0)/triggered*100:.1f}% |

### 问题统计

| 级别 | 数量 |
|------|------|
| P0 | {issue_counts.get('P0', 0)} |
| P1 | {issue_counts.get('P1', 0)} |
| P2 | {issue_counts.get('P2', 0)} |

### Top 5 高频触发语句

"""
    for i, (query, count) in enumerate(query_counts.most_common(5), 1):
        report += f"{i}. `{query}` ({count}次)\n"
    
    report += "\n### 每日趋势\n\n"
    report += "| 日期 | 总 query | 触发 | 误触发 | 接受率 |\n"
    report += "|------|----------|------|--------|--------|\n"
    
    for date in dates:
        day_logs = load_logs(date)
        day_total = len(day_logs)
        day_triggered = sum(1 for l in day_logs if l.get('triggered', False))
        day_false = sum(1 for l in day_logs if l.get('false_positive', False))
        day_accepted = sum(1 for l in day_logs if l.get('user_accepted', False))
        day_accept_rate = (day_accepted / day_triggered * 100) if day_triggered > 0 else 0
        report += f"| {date} | {day_total} | {day_triggered} | {day_false} | {day_accept_rate:.1f}% |\n"
    
    return report

def log_query(query, triggered, false_positive=False, routed_layer=None, 
              user_accepted=None, clear_next_step=None, issue_level=None, notes=""):
    """记录单条 query 日志"""
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "query": query,
        "triggered": triggered,
        "false_positive": false_positive,
        "routed_layer": routed_layer,
        "user_accepted": user_accepted,
        "clear_next_step": clear_next_step,
        "issue_level": issue_level,
        "notes": notes
    }
    
    today = datetime.now().strftime('%Y-%m-%d')
    log_path = LOGS_DIR / f"triggers_{today}.jsonl"
    
    with open(log_path, 'a', encoding='utf-8') as f:
        f.write(json.dumps(log_entry, ensure_ascii=False) + '\n')
    
    return log_entry

def main():
    parser = argparse.ArgumentParser(description='openclaw-onboarding-guide 监控脚本')
    parser.add_argument('--daily', action='store_true', help='生成日报')
    parser.add_argument('--weekly', action='store_true', help='生成周报')
    parser.add_argument('--today', action='store_true', help='查看今日实时数据')
    parser.add_argument('--date', type=str, help='指定日期 (YYYY-MM-DD)')
    parser.add_argument('--log', type=str, help='记录单条 query')
    parser.add_argument('--triggered', action='store_true', help='是否触发 (与 --log 配合)')
    parser.add_argument('--layer', type=str, help='路由层级 (L1-L5, 与 --log 配合)')
    parser.add_argument('--issue', type=str, help='问题级别 (P0/P1/P2, 与 --log 配合)')
    
    args = parser.parse_args()
    
    # 记录单条日志
    if args.log:
        entry = log_query(
            query=args.log,
            triggered=args.triggered,
            routed_layer=args.layer,
            issue_level=args.issue
        )
        print(f"Logged: {entry['query']}")
        return
    
    # 今日实时
    if args.today:
        today = datetime.now().strftime('%Y-%m-%d')
        logs = load_logs(today)
        print(generate_daily_report(today, logs))
        return
    
    # 日报
    if args.daily:
        date = args.date or datetime.now().strftime('%Y-%m-%d')
        logs = load_logs(date)
        report = generate_daily_report(date, logs)
        print(report)
        
        # 自动保存到文件
        output_path = LOGS_DIR / f"daily_{date}.md"
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"\nSaved to: {output_path}")
        return
    
    # 周报
    if args.weekly:
        if args.date:
            week_start = datetime.strptime(args.date, '%Y-%m-%d')
        else:
            # 本周一
            today = datetime.now()
            week_start = today - timedelta(days=today.weekday())
        
        report = generate_weekly_report(week_start)
        print(report)
        
        # 自动保存到文件
        week_str = week_start.strftime('%Y-W%W')
        output_path = LOGS_DIR / f"week_{week_str}.md"
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"\nSaved to: {output_path}")
        return
    
    # 默认显示帮助
    parser.print_help()

if __name__ == '__main__':
    main()
