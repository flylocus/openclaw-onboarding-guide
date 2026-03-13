# 🎉 openclaw-onboarding-guide 测试邀请

**版本：** v1.1（Phase 3 验证版）  
**状态：** 已公开，欢迎测试！  
**仓库：** https://github.com/flylocus/openclaw-onboarding-guide

---

## 📦 快速安装

### 前提条件

- ✅ 已安装 OpenClaw 或 Copaw
- ✅ 有 GitHub 账号（用于 SSH 认证）

### 安装步骤

```bash
# 1. 进入技能目录
cd ~/.openclaw/skills/

# 2. 克隆仓库
git clone https://github.com/flylocus/openclaw-onboarding-guide.git

# 3. 验证安装
ls openclaw-onboarding-guide/SKILL.md

# 4. 重启 OpenClaw/Copaw
```

---

## 🧪 测试用例

安装后，试试发送以下消息：

### 测试 1：新用户引导
```
我第一次用 OpenClaw，从哪开始？
```
**预期：** 引导你到 L1（系统如何工作）

---

### 测试 2：具体任务
```
我想写代码
```
**预期：** 路由到 L3（执行工具）

---

### 测试 3：自动化场景（P0 规则触发）
```
我想自动化这个流程
```
**预期：** 先追问是"一次性自动化"还是"长期系统"

---

### 测试 4：长期系统（P1 规则触发）
```
我想搭一个长期系统
```
**预期：** 先解释结构重要性，再路由到 L1

---

## 📝 反馈方式

遇到问题或有建议？用 Issue 模板提交：

### 🐛 Bug 报告
技能无法使用、路由错误、系统崩溃  
→ https://github.com/flylocus/openclaw-onboarding-guide/issues/new?template=bug_report.md

### 📝 测试反馈
使用体验、摩擦点、改进建议  
→ https://github.com/flylocus/openclaw-onboarding-guide/issues/new?template=feedback.md

### 💡 功能请求
新功能建议、场景扩展  
→ https://github.com/flylocus/openclaw-onboarding-guide/issues/new?template=feature_request.md

---

## 📊 测试周期

| 阶段 | 时间 | 目标 |
|------|------|------|
| **Phase A** | 2026-03-15 ~ 2026-03-28 | 收集 ≥50 条真实 query |
| **Phase B** | 2026-03-29 ~ 2026-04-05 | 分析数据，发布 v1.2 |
| **Phase C** | 2026-04-06+ | 决定是否接入 ClawHub 市场 |

---

## 🎯 核心指标

| 指标 | 目标值 | 说明 |
|------|--------|------|
| 触发准确率 | ≥90% | 应该触发时触发的比例 |
| 路由接受率 | ≥80% | 用户按推荐继续的比例 |
| 误触发率 | <10% | 不该触发时触发的比例 |
| 用户追问率 | 自然 | >50% 需检查引导是否清晰 |

---

## 🔗 相关资源

- **GitHub 仓库：** https://github.com/flylocus/openclaw-onboarding-guide
- **完整文档：** https://github.com/flylocus/openclaw-onboarding-guide/blob/main/README.md
- **Issue 列表：** https://github.com/flylocus/openclaw-onboarding-guide/issues
- **作者：** 申飞 (@flylocus)

---

## 💬 常见问题

### Q: 这个技能做什么？
A: 帮新用户快速找到合适的 OpenClaw 入口，不会在一大堆功能里迷路。

### Q: 和直接看技能列表有什么区别？
A: 不是给列表，而是先分类你的问题类型，再推荐 1-3 个具体动作。

### Q: 为什么会触发追问？
A: "自动化"和"长期系统"太模糊，追问是为了更准确路由。

### Q: 如何更新？
A: `cd ~/.openclaw/skills/openclaw-onboarding-guide && git pull`

---

**感谢参与测试！** 🙏  
你的每一个反馈都会让产品更好用。

有任何问题随时提 Issue 或联系我！

---

**飞哥备注：** 这是封闭测试版，仅邀请 3-5 位朋友参与。测试结束后决定是否公开发布到 ClawHub 市场。
