# 轻量监控脚本需求单 v1

**用途:** 自动统计 openclaw-onboarding-guide 每日触发数据  
**复杂度:** 最小可用 (MVP)  
**开发时间:** ≤2 小时

---

## 一、核心需求

### 功能 1: 自动计数

**输入:** 日志文件 (JSONL 格式)  
**输出:** 当日汇总数据

**统计项:**
1. 总 query 数
2. 触发次数
3. 误触发次数
4. 各层级路由次数 (L1/L2/L3/L4/L5)
5. P0/P1/P2 问题数

---

### 功能 2: 每日汇总输出

**输出格式:** Markdown 表格

```markdown
## 2026-03-15 汇总

| 指标 | 数值 |
|------|------|
| 总 query 数 | __ |
| 触发次数 | __ |
| 误触发 | __ |
| L1 路由 | __ |
| L2 路由 | __ |
| L3 路由 | __ |
| L4 路由 | __ |
| L5 路由 | __ |
| P0 问题 | __ |
| P1 问题 | __ |
| P2 问题 | __ |
```

---

### 功能 3: 每周汇总

**输入:** 7 天每日数据  
**输出:** 周汇总报告

**统计项:**
1. 周总 query 数
2. 周总触发数
3. 平均触发准确率
4. 平均路由接受率
5. Top 5 高频 query
6. Top 3 路由层级

---

## 二、日志格式规范

### 日志文件位置

```
~/.openclaw/skills/openclaw-onboarding-guide/logs/triggers_YYYY-MM-DD.jsonl
```

### 单条日志格式

```json
{
  "timestamp": "2026-03-15T10:30:00+08:00",
  "query": "用户原始输入",
  "triggered": true,
  "false_positive": false,
  "routed_layer": "L1",
  "user_accepted": true,
  "clear_next_step": true,
  "issue_level": null,
  "notes": ""
}
```

### 字段说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| timestamp | string | ✅ | ISO 8601 时间戳 |
| query | string | ✅ | 用户原始输入 |
| triggered | boolean | ✅ | 是否触发 skill |
| false_positive | boolean | ✅ | 是否误触发 |
| routed_layer | string | ❌ | L1/L2/L3/L4/L5 (仅触发时) |
| user_accepted | boolean | ❌ | 用户是否接受推荐 |
| clear_next_step | boolean | ❌ | 用户是否知道下一步 |
| issue_level | string | ❌ | P0/P1/P2/null |
| notes | string | ❌ | 备注 |

---

## 三、脚本技术需求

### 运行环境

- **语言:** Python 3.10+
- **依赖:** 仅标准库 (json, datetime, collections)
- **执行方式:** 命令行或 cron

---

### 脚本命令

```bash
# 生成日报
python monitor.py --daily --date 2026-03-15

# 生成周报
python monitor.py --weekly --week 2026-W12

# 实时查看今日
python monitor.py --today
```

---

### 输出位置

```
~/.openclaw/skills/openclaw-onboarding-guide/logs/
├── daily_2026-03-15.md
├── daily_2026-03-16.md
├── ...
├── week_2026-W12.md
└── summary.md (累计汇总)
```

---

## 四、最小功能清单

### Must Have (P0)

- [ ] 读取 JSONL 日志
- [ ] 统计触发次数
- [ ] 统计误触发
- [ ] 统计路由层级分布
- [ ] 输出 Markdown 日报

### Should Have (P1)

- [ ] 周汇总功能
- [ ] Top query 统计
- [ ] 自动写入文件

### Nice to Have (P2)

- [ ] 累计汇总
- [ ] 简单图表 (文本)
- [ ] Cron 自动执行

---

## 五、开发优先级

### Phase 1 (03-15 前完成)

1. 日志格式定义 ✅ (本文档)
2. 手动记录模板 ✅ (data_sheet_v1.md)
3. 脚本框架搭建

### Phase 2 (03-17 前完成)

1. 日报功能完成
2. 周汇总功能完成
3. 测试验证

### Phase 3 (03-21 前完成)

1. Cron 自动执行
2. 累计汇总
3. 优化输出格式

---

## 六、验收标准

### 功能验收

| 测试项 | 预期结果 | 实际结果 |
|--------|----------|----------|
| 读取 10 条日志 | 正确解析 | |
| 统计触发数 | 准确计数 | |
| 统计误触发 | 准确计数 | |
| 路由层级分布 | 准确分类 | |
| 输出 Markdown | 格式正确 | |

### 性能验收

| 指标 | 目标 | 实际 |
|------|------|------|
| 处理 100 条日志 | <1 秒 | |
| 处理 1000 条日志 | <5 秒 | |
| 内存占用 | <50MB | |

---

## 七、示例代码框架

```python
#!/usr/bin/env python3
"""
openclaw-onboarding-guide 监控脚本 v1
轻量级数据统计工具
"""

import json
from datetime import datetime
from collections import Counter
from pathlib import Path

def load_logs(date_str):
    """读取指定日期的日志"""
    log_path = Path(f"logs/triggers_{date_str}.jsonl")
    if not log_path.exists():
        return []
    
    logs = []
    with open(log_path, 'r') as f:
        for line in f:
            logs.append(json.loads(line))
    return logs

def generate_daily_report(date_str, logs):
    """生成日报"""
    total = len(logs)
    triggered = sum(1 for l in logs if l['triggered'])
    false_pos = sum(1 for l in logs if l['false_positive'])
    
    layer_counts = Counter(l['routed_layer'] for l in logs if l.get('routed_layer'))
    issue_counts = Counter(l['issue_level'] for l in logs if l.get('issue_level'))
    
    report = f"""## {date_str} 汇总

| 指标 | 数值 |
|------|------|
| 总 query 数 | {total} |
| 触发次数 | {triggered} |
| 误触发 | {false_pos} |
| L1 路由 | {layer_counts.get('L1', 0)} |
| L2 路由 | {layer_counts.get('L2', 0)} |
| L3 路由 | {layer_counts.get('L3', 0)} |
| L4 路由 | {layer_counts.get('L4', 0)} |
| L5 路由 | {layer_counts.get('L5', 0)} |
| P0 问题 | {issue_counts.get('P0', 0)} |
| P1 问题 | {issue_counts.get('P1', 0)} |
| P2 问题 | {issue_counts.get('P2', 0)} |
"""
    return report

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--daily', action='store_true')
    parser.add_argument('--date', type=str)
    args = parser.parse_args()
    
    if args.daily and args.date:
        logs = load_logs(args.date)
        report = generate_daily_report(args.date, logs)
        print(report)

if __name__ == '__main__':
    main()
```

---

## 八、负责人与时间

| 任务 | 负责人 | 截止日期 | 状态 |
|------|--------|----------|------|
| 日志格式定义 | [待定] | 03-14 | ✅ |
| 脚本框架 | [待定] | 03-15 | |
| 日报功能 | [待定] | 03-17 | |
| 周汇总功能 | [待定] | 03-17 | |
| 测试验证 | [待定] | 03-18 | |
| Cron 配置 | [待定] | 03-21 | |

---

**版本:** v1  
**创建日期:** 2026-03-14  
**目标完成:** 03-17 (日报 + 周汇总)  
**文档位置:** `~/.openclaw/skills/openclaw-onboarding-guide/logs/monitor_requirements_v1.md`
