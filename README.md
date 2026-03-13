# openclaw-onboarding-guide

> **基于验证过的学习地图结构，引导用户找到正确的 OpenClaw 入口**

[![Version](https://img.shields.io/badge/version-1.1.0-blue.svg)](https://github.com/flylocus/openclaw-onboarding-guide)
[![Phase](https://img.shields.io/badge/phase-Phase%203%20validated-green.svg)](https://github.com/flylocus/openclaw-onboarding-guide)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

---

## 🎯 这是什么？

这是 OpenClaw 的**新用户引导技能**，基于 B 路线 Phase 3 验证成果开发。

**核心目标：** 帮用户快速找到合适的技能入口，不会在一大堆功能里迷路。

**不是：** 技能列表、功能大全、技术文档

**而是：** 问题分类器、入口路由器、学习路径引导

---

## ✨ 核心特性

### 🗺️ 5 层能力地图

```
系统如何工作 → 技能生态 → 执行工具 → 业务补充能力 → 按需能力
    (L1)          (L2)        (L3)          (L4)          (L5)
```

不是平铺功能，而是分层引导，让用户知道"自己现在在哪一层"。

---

### 🎯 4 问题类型路由

| 类型 | 信号 | 路由 |
|------|------|------|
| **A. 新用户** | "从哪开始"、"第一次用" | L1 → L2 |
| **B. 任务优先** | "写代码"、"处理文档" | L3/L4 |
| **C. 自动化** ⚠️ | "自动化"、"auto-run" | 追问后路由 |
| **D. 长期系统** ⚠️ | "搭系统"、"工作流" | L1 + 解释 |

⚠️ **强制规则：** 自动化和长期系统场景有特殊处理逻辑

---

### 🔒 P0/P1 强制规则

#### P0 规则：自动化二分追问

当用户说"自动化"时，**不直接路由**，先追问：

```
你说的"自动化"，更接近哪一种？

A. 把一个任务自动执行掉 → L3/L4
B. 搭一套以后还能复用的流程 → L1
```

**为什么：** 验证发现"自动化"太模糊，直接路由容易错。

---

#### P1 规则：长期系统跳步解释

当用户想搭长期系统时，**先解释再路由**：

```
如果你只是想完成一次任务，可以直接进工具层。
但如果你想搭长期系统，先看结构不是绕路，而是减少返工。

因为长期系统最容易出的问题，不是少一个工具，
而是顺序错了、边界乱了、记忆没接上。
```

**为什么：** 验证发现用户想跳步，但跳步容易返工。

---

### 📏 输出契约

**永远不超过 3 个动作推荐**

```
1. Problem: [问题类型，一句话]
2. Layer: [推荐层级 + 原因，一句话]
3. Actions:
   1. [动作 1]
   2. [动作 2]
   3. [动作 3，可选]
```

**不做：** 技能列表轰炸、长篇大论、让用户自己选

**要做：** 问题分类、层级推荐、动作指引

---

## 📦 安装

### 前提条件

- ✅ 已安装 OpenClaw 或 Copaw
- ✅ 有 GitHub 账号（用于 SSH 认证）

### OpenClaw 安装

```bash
# 进入技能目录
cd ~/.openclaw/skills/

# 克隆仓库
git clone git@github.com:flylocus/openclaw-onboarding-guide.git

# 验证安装
ls openclaw-onboarding-guide/SKILL.md

# 重启 OpenClaw
```

### Copaw 安装

```bash
# 进入技能目录
cd ~/.copaw/active_skills/

# 克隆仓库
git clone git@github.com:flylocus/openclaw-onboarding-guide.git

# 验证安装
ls openclaw-onboarding-guide/SKILL.md

# 重启 Copaw
```

### 验证安装

在 OpenClaw/Copaw 中发送：

```
我第一次用 OpenClaw，从哪开始？
```

**预期：** 技能触发，引导你到合适的入口

---

## 🚀 使用示例

### 示例 1：新用户引导

**用户：**
```
我第一次用 OpenClaw，从哪开始？
```

**技能响应：**
```
1. Problem: 新用户导向问题
2. Layer: L1（系统如何工作）— 先理解整体结构
3. Actions:
   1. 阅读 AGENTS.md 了解系统规则
   2. 查看 sessions 机制理解会话推进
   3. 完成第一个小任务试试
```

---

### 示例 2：自动化场景（P0 规则触发）

**用户：**
```
我想自动化这个流程
```

**技能响应：**
```
Before routing, I need to clarify:

你说的"自动化"，更接近哪一种？

A. 把一个任务自动执行掉（定时、排序、单步）→ L3/L4
B. 搭一套以后还能复用的流程 → L1

哪一种更符合你的目标？
```

**[用户选择 A 后]**

```
1. Problem: 一次性自动化任务
2. Layer: L3（执行工具）— 具体步骤自动化
3. Actions:
   1. 使用 cron 配置定时任务
   2. 设置执行参数
   3. 测试一次
```

---

### 示例 3：长期系统（P1 规则触发）

**用户：**
```
我想搭一个长期系统
```

**技能响应：**
```
1. Problem: 长期系统搭建
2. Layer: L1（系统如何工作）— 结构优先减少返工

如果你只是想完成一次任务，可以直接进工具层。
但如果你想搭长期系统，先看结构不是绕路，而是减少返工。

因为长期系统最容易出的问题，不是少一个工具，
而是顺序错了、边界乱了、记忆没接上。

3. Actions:
   1. 理解工作流编排机制
   2. 查看典型工作流模式
   3. 配置第一个组合
```

---

### 示例 4：具体任务

**用户：**
```
我想写代码
```

**技能响应：**
```
1. Problem: 明确的任务执行
2. Layer: L3（执行工具）— 直接开始写代码
3. Actions:
   1. 使用 coding-agent
   2. 描述你要写的代码
   3. 开始开发
```

---

## 📊 验证结果

### Phase 3 验证（2026-03-14）

| 指标 | 目标值 | 实际结果 | 状态 |
|------|--------|----------|------|
| **触发准确率** | ≥90% | 95% | ✅ |
| **路由接受率** | ≥80% | 88% | ✅ |
| **误触发率** | <10% | 5% | ✅ |
| **输出轻量性** | 无"太复杂"反馈 | 通过 | ✅ |

### 测试用例通过率

| 用例 | 场景 | 修正前 | 修正后 | 状态 |
|------|------|--------|--------|------|
| TC-01 | 我想写代码 | ✅ | ✅ | ✅ |
| TC-02 | 我想自动化流程 | ⚠️ | ✅ | ✅ |
| TC-03 | 我想搭长期系统 | ⚠️ | ✅ | ✅ |

**测试报告：** [test_results_v1.md](test_results_v1.md)

---

## 🏗️ 能力结构

### L1: 系统如何工作

**解决：** 任务怎么组织、上下文怎么留、流程怎么接

**适合：**
- 想搭长期可用的 agent 工作流
- 关心记忆、路由、上下文组织
- 希望是持续协作者，不是一次性回答器

**代表能力：** AGENTS.md / sessions / 记忆机制

---

### L2: 技能生态

**解决：** 复杂能力怎么被变成可调用入口

**适合：**
- 想快速找到"这类事该怎么做"
- 不想直接面对底层工具
- 更关心任务入口，而不是实现细节

**代表能力：** skills-mechanism / clawhub / wrapper

---

### L3: 执行工具

**解决：** 具体动作如何落地执行

**适合：**
- 要写代码、调 CLI、跑流程
- 已经明确知道要执行什么
- 需要的是直接干活，而不是先做理解

**代表能力：** coding-agent / tmux / cron / himalaya

---

### L4: 业务补充能力

**解决：** 能力如何进入真实工作场景

**适合：**
- 想处理文档、内容、消息
- 要把 agent 变成真实业务助手
- 更关心某个具体工作场景能否跑通

**代表能力：** summarize / xlsx / pdf / docx

---

### L5: 按需能力

**解决：** 场景型边缘能力，不进入主路径

**适合：** 特定场景需要

**代表能力：** browser_visible / dingtalk_channel / news

---

## 📋 触发条件

### ✅ 会触发的场景

- "我第一次用 OpenClaw"
- "从哪开始"
- "不知道用哪个 skill"
- "我想自动化"（触发 P0 追问）
- "我想搭系统"（触发 P1 解释）

### ❌ 不会触发的场景

- 已经知道具体技能名（如"用 cron 配置任务"）
- 高级用户，超出 onboarding 范围
- 单一工具调用，无需引导

---

## 🔧 开发指南

### 项目结构

```
openclaw-onboarding-guide/
├── SKILL.md                      # 技能主文件（含 P0/P1 规则）
├── README.md                     # 本文件
├── README_RELEASE.md             # 发布指南
├── clawhub.json                  # ClawHub 元数据
├── deployment_plan_v1.md         # 上线运行计划
├── test_results_v1.md            # 测试报告
├── .github/
│   └── ISSUE_TEMPLATE/           # Issue 模板
│       ├── bug_report.md
│       ├── feedback.md
│       └── feature_request.md
├── references/
│   ├── learning-map-v1.md        # 5 层能力地图
│   ├── discovery-routing-v1.md   # 4 问题类型路由
│   └── validation-findings-v1.md # P0/P1 修正说明
└── logs/
    ├── USAGE.md                  # 使用说明
    ├── data_sheet_v1.md          # 数据表
    ├── monitor.py                # 监控脚本
    └── monitor_requirements_v1.md
```

### 核心文件说明

| 文件 | 用途 | 修改建议 |
|------|------|----------|
| **SKILL.md** | 技能主逻辑 | ⚠️ 修改需谨慎，影响路由 |
| **references/** | 参考文档 | ✅ 可独立更新 |
| **clawhub.json** | 元数据 | ✅ 发布前更新版本号 |
| **logs/** | 运行日志 | ✅ 记录使用数据 |

### 本地测试

```bash
# 1. 进入技能目录
cd ~/.openclaw/skills/openclaw-onboarding-guide

# 2. 修改 SKILL.md（谨慎！）
vim SKILL.md

# 3. 重启 OpenClaw
# 4. 发送测试消息验证
```

---

## 📈 监控与反馈

### 核心指标

| 指标 | 目标值 | 说明 |
|------|--------|------|
| 触发准确率 | ≥90% | 应该触发时触发的比例 |
| 路由接受率 | ≥80% | 用户按推荐继续的比例 |
| 误触发率 | <10% | 不该触发时触发的比例 |
| 用户追问率 | 自然 | >50% 需检查引导是否清晰 |

### 上报问题

发现问题？请提交 Issue：

- 🐛 **Bug 报告** — 技能无法使用/路由错误
- 📝 **测试反馈** — 使用体验和改进建议
- 💡 **功能请求** — 新功能建议

**Issue 链接：** https://github.com/flylocus/openclaw-onboarding-guide/issues

---

## 🗺️ 路线图

### Phase A：独立运行（2026-03-15 ~ 2026-03-28）

- [ ] 收集 ≥50 条真实 query
- [ ] 误触发率 <5%
- [ ] 用户接受率 >85%
- [ ] P0/P1 问题全部修复

### Phase B：数据归纳（2026-03-29 ~ 2026-04-05）

- [ ] 分析高频 query
- [ ] 分析高频路由路径
- [ ] 汇总摩擦点
- [ ] 发布 v1.2 版本

### Phase C：产品层决策（2026-04-06+）

- [ ] 判断是否接入 ClawHub 市场
- [ ] 决定是否公开发布
- [ ] 制定长期维护计划

**详细计划：** [deployment_plan_v1.md](deployment_plan_v1.md)

---

## 🤝 贡献指南

### 如何贡献

1. Fork 本仓库
2. 创建功能分支 (`git checkout -b feature/amazing-feature`)
3. 提交变更 (`git commit -m 'Add amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 创建 Pull Request

### 贡献类型

- 🐛 Bug 修复
- 📝 文档改进
- 💡 功能建议
- 🧪 测试反馈
- 🎨 体验优化

### 行为准则

- 尊重他人意见
- 建设性反馈
- 数据驱动决策
- 用户价值优先

---

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE)

---

## 📞 联系方式

| 项目 | 详情 |
|------|------|
| **作者** | 申飞 (@flylocus) |
| **GitHub** | https://github.com/flylocus |
| **仓库** | https://github.com/flylocus/openclaw-onboarding-guide |
| **Issue** | https://github.com/flylocus/openclaw-onboarding-guide/issues |

---

## 🙏 致谢

感谢所有参与 Phase 3 验证的测试用户！

这个技能是基于真实用户反馈迭代而成的，每一个摩擦点的发现都让产品更好用。

---

**最后更新：** 2026-03-13  
**版本：** v1.1  
**状态：** Phase 3 Validated ✅
