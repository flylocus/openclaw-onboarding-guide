# 监控脚本快速使用指南

**脚本位置:** `logs/monitor.py`  
**Python 版本:** 3.10+  
**依赖:** 仅标准库

---

## 一、记录单条 query

### 基础用法

```bash
# 触发成功，路由到 L1
python3 monitor.py --log "用户 query" --triggered --layer L1

# 触发成功，路由到 L3
python3 monitor.py --log "我想写代码" --triggered --layer L3

# 未触发
python3 monitor.py --log "老用户问具体技能" --triggered

# 误触发
python3 monitor.py --log "不该触发的 query" --triggered --layer L2

# 有问题
python3 monitor.py --log "路由错了" --triggered --layer L3 --issue P0
```

### 参数说明

| 参数 | 说明 | 必填 |
|------|------|------|
| `--log` | 用户原始 query | ✅ |
| `--triggered` | 是否触发 skill | ✅ |
| `--layer` | 路由层级 (L1-L5) | 触发时必填 |
| `--issue` | 问题级别 (P0/P1/P2) | 有问题时填 |

---

## 二、查看数据

### 今日实时

```bash
python3 monitor.py --today
```

### 指定日期日报

```bash
python3 monitor.py --daily --date 2026-03-15
```

### 本周周报

```bash
python3 monitor.py --weekly
```

### 指定周周报

```bash
python3 monitor.py --weekly --date 2026-03-17
```

---

## 三、输出文件

| 类型 | 文件名 | 位置 |
|------|--------|------|
| 原始日志 | `triggers_YYYY-MM-DD.jsonl` | `logs/` |
| 日报 | `daily_YYYY-MM-DD.md` | `logs/` |
| 周报 | `week_YYYY-Www.md` | `logs/` |

---

## 四、快速记录模板

### 复制粘贴用

```bash
# 新手引导 (L1)
python3 monitor.py --log "query" --triggered --layer L1

# skill 选择 (L2)
python3 monitor.py --log "query" --triggered --layer L2

# 执行工具 (L3)
python3 monitor.py --log "query" --triggered --layer L3

# 业务能力 (L4)
python3 monitor.py --log "query" --triggered --layer L4

# 误触发
python3 monitor.py --log "query" --triggered --layer LX

# P0 问题
python3 monitor.py --log "query" --triggered --layer L3 --issue P0
```

---

## 五、每日工作流程

### 早上

```bash
# 查看昨日日报
python3 monitor.py --daily --date YYYY-MM-DD
```

### 随时

```bash
# 记录每条触发的 query
python3 monitor.py --log "用户输入" --triggered --layer L1
```

### 晚上

```bash
# 查看今日汇总
python3 monitor.py --today
```

---

## 六、示例会话

### 示例 1: 新手用户

```bash
# 用户问
python3 monitor.py --log "我第一次用，从哪开始" --triggered --layer L1

# 用户接受推荐
# (手动更新日志文件添加 user_accepted: true)
```

### 示例 2: 自动化追问

```bash
# 用户说"我想自动化"
python3 monitor.py --log "我想自动化流程" --triggered --layer L1

# 用户选择 A (一次性)
# 记录后续行为
```

### 示例 3: 误触发

```bash
# 老用户问具体技能，不应该触发
python3 monitor.py --log "cron 怎么用" --triggered --issue P0
```

---

## 七、数据检查

### 检查日志文件

```bash
# 查看今日原始日志
cat logs/triggers_$(date +%Y-%m-%d).jsonl
```

### 检查文件列表

```bash
ls -la logs/*.jsonl logs/*.md
```

---

## 八、常见问题

### Q: 记录错了怎么办？

A: 直接编辑 `triggers_YYYY-MM-DD.jsonl` 文件，删除或修改错误行。

### Q: 如何批量导入？

A: 按 JSONL 格式准备数据，每行一个 JSON 对象，追加到日志文件。

### Q: 周报从哪天开始算？

A: 每周一为一周开始，自动计算。

---

**版本:** v1  
**创建:** 2026-03-14  
**状态:** ✅ 测试通过
