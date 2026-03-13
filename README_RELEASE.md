# openclaw-onboarding-guide 发布指南

**版本：** v1.1（收敛版）  
**打包时间：** 2026-03-13  
**状态：** ✅ Phase 3 验证通过，可发布测试

---

## 一、技能包内容

```
openclaw-onboarding-guide/
├── SKILL.md                      # 技能主文件（含 P0/P1 规则）
├── deployment_plan_v1.md         # 上线运行计划
├── test_results_v1.md            # 测试报告（6/6 通过）
├── README_RELEASE.md             # 本文件
├── references/
│   ├── learning-map-v1.md        # 5 层能力地图
│   ├── discovery-routing-v1.md   # 4 问题类型路由
│   └── validation-findings-v1.md # P0/P1 修正说明
└── logs/                         # 运行日志（可选）
```

**打包大小：** ~18KB  
**核心文件：** SKILL.md + references/（3 个文件）

---

## 二、安装方式

### 方式 A：直接复制（推荐测试用）

```bash
# 1. 解压技能包
tar -xzf openclaw-onboarding-guide.tar.gz

# 2. 复制到 Copaw 技能目录
cp -r openclaw-onboarding-guide ~/.copaw/active_skills/

# 3. 重启 Copaw
# （技能会在下次启动时自动加载）
```

### 方式 B：Git 安装（推荐正式用）

```bash
# 1. Clone 技能仓库
cd ~/.copaw/active_skills/
git clone https://github.com/YOUR_USERNAME/openclaw-onboarding-guide.git

# 2. 重启 Copaw
```

---

## 三、发布渠道选择

### 选项 1：GitHub 私有仓库（推荐内部测试）

**适合：** 小范围测试、朋友间分享

**步骤：**
1. 创建 GitHub 私有仓库
2. 推送技能文件
3. 给朋友 GitHub 访问权限
4. 朋友用 Git 方式安装

**优点：**
- ✅ 版本管理清晰
- ✅ 可随时更新
- ✅ 访问权限可控

**缺点：**
- ⚠️ 需要 GitHub 账号
- ⚠️ 需要配置访问权限

---

### 选项 2：GitHub 公开仓库（推荐开源发布）

**适合：** 公开分享、社区贡献

**步骤：**
1. 创建 GitHub 公开仓库
2. 添加 LICENSE（推荐 MIT）
3. 完善 README.md（使用说明）
4. 添加 ClawHub 元数据（可选）

**优点：**
- ✅ 完全开放
- ✅ 可接受社区贡献
- ✅ 易于传播

**缺点：**
- ⚠️ 代码完全公开
- ⚠️ 无法控制使用范围

---

### 选项 3：直接分享压缩包（最快）

**适合：** 一对一分享、快速测试

**步骤：**
1. 发送 `openclaw-onboarding-guide.tar.gz`
2. 朋友解压后复制到 `~/.copaw/active_skills/`
3. 重启 Copaw

**优点：**
- ✅ 最简单
- ✅ 无需额外工具
- ✅ 即时可用

**缺点：**
- ⚠️ 无版本管理
- ⚠️ 更新需重新发送
- ⚠️ 不适合大规模分发

---

### 选项 4：ClawHub 技能市场（推荐正式发布）

**适合：** 官方发布、社区发现

**步骤：**
1. 准备 ClawHub 元数据（`clawhub.json`）
2. 提交到 ClawHub 审核
3. 通过后上架技能市场

**优点：**
- ✅ 官方背书
- ✅ 用户发现容易
- ✅ 自动更新支持

**缺点：**
- ⚠️ 需审核流程
- ⚠️ 需符合 ClawHub 规范
- ⚠️ 当前可能还在开发中

---

## 四、推荐发布流程（给朋友测试）

### 第一阶段：小范围测试（现在）

**目标：** 3-5 个朋友测试，收集反馈

**方式：** 直接分享压缩包 + 私有 GitHub

**步骤：**
1. ✅ 打包完成（`openclaw-onboarding-guide.tar.gz`）
2. 创建 GitHub 私有仓库
3. 推送代码
4. 发送压缩包给第一批测试用户
5. 收集使用反馈

**时间：** 1-2 周

---

### 第二阶段：修正优化（根据反馈）

**目标：** 修复 P0/P1 问题，优化体验

**方式：** GitHub Issues + 版本迭代

**步骤：**
1. 收集测试反馈
2. 优先级分类（P0/P1/P2）
3. 修复 P0 问题（触发/路由错误）
4. 发布 v1.2 版本

**时间：** 1 周

---

### 第三阶段：公开发布（可选）

**目标：** 社区发布，接受更多用户

**方式：** GitHub 公开 + ClawHub 上架

**步骤：**
1. 转为公开仓库
2. 完善文档（README/使用示例/FAQ）
3. 提交 ClawHub 审核
4. 正式发布

**时间：** 视情况而定

---

## 五、给测试用户的安装说明

### 快速安装（3 步）

```bash
# 1. 解压
tar -xzf openclaw-onboarding-guide.tar.gz

# 2. 复制
cp -r openclaw-onboarding-guide ~/.copaw/active_skills/

# 3. 重启 Copaw
# 完成！
```

### 验证安装

```bash
# 检查文件是否存在
ls ~/.copaw/active_skills/openclaw-onboarding-guide/SKILL.md

# 检查 YAML 格式（可选）
python3 -c "import yaml; yaml.safe_load(open('~/.copaw/active_skills/openclaw-onboarding-guide/SKILL.md').read().split('---')[1])"
```

### 测试使用

在 Copaw 中发送以下消息测试：

```
"我第一次用 OpenClaw，从哪开始？"
"我想自动化这个流程"
"我想搭一个长期系统"
```

**预期行为：**
- 技能正确触发
- 按照 P0/P1 规则分流
- 输出不超过 3 个动作推荐

---

## 六、反馈收集模板

### 问题上报格式

```markdown
## 问题描述
[简要说明遇到的问题]

## 触发语句
[你发送了什么消息]

## 预期行为
[你期望发生什么]

## 实际行为
[实际发生了什么]

## 截图/日志（可选）
[如有，请附加]

## 优先级判断
- [ ] P0：技能无法使用/路由错误
- [ ] P1：输出过重/解释不清
- [ ] P2：边界情况/建议
```

### 反馈渠道

- GitHub Issues（推荐）
- 邮件/微信（快速反馈）
- 共享文档（集中收集）

---

## 七、版本历史

| 版本 | 日期 | 变更 | 状态 |
|------|------|------|------|
| v1.1 | 2026-03-13 | 修复 YAML frontmatter 格式 | ✅ 已发布 |
| v1.0 | 2026-03-13 | Phase 3 验证完成 | ✅ 已验证 |

---

## 八、常见问题

### Q1: 安装后技能不触发？

**A:** 检查以下几点：
1. 文件路径是否正确（`~/.copaw/active_skills/openclaw-onboarding-guide/SKILL.md`）
2. 是否重启了 Copaw
3. 检查日志是否有加载错误

### Q2: 触发但不按预期分流？

**A:** 可能是触发条件问题，请：
1. 记录触发语句
2. 检查是否匹配 Trigger Conditions
3. 上报反馈用于优化

### Q3: 如何更新到新版本？

**A:** 
```bash
# 删除旧版本
rm -rf ~/.copaw/active_skills/openclaw-onboarding-guide

# 安装新版本
tar -xzf openclaw-onboarding-guide_v1.2.tar.gz
cp -r openclaw-onboarding-guide ~/.copaw/active_skills/

# 重启 Copaw
```

---

## 九、联系与支持

**技能维护者：** [你的名字]  
**GitHub:** [你的 GitHub 地址]  
**邮箱：** [你的邮箱]  

**问题上报：** GitHub Issues（推荐）或邮件

---

**最后更新：** 2026-03-13  
**文档版本：** v1.0
