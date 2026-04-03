<div align="center">

# 教授.skill

> *“教授不必永远在线，但学术风格可以被继承。”*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://python.org)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![AgentSkills](https://img.shields.io/badge/AgentSkills-Standard-green)](https://agentskills.io)

<br>

学生会毕业，课题会结题，导师也不可能 24 小时在线。<br>
但论文、报告、讲义、演讲、批注、方法论——这些不会。<br>
**教授.skill** 不是“复活真人”，而是把一位教授的研究知识、学术风格、指导偏好和方法论，蒸馏成一个可交互的科研智能体。<br>

它既能基于教授自己的论文和材料给学生做指导，<br>
也能结合大模型通识能力、外部论文检索结果与当前任务上下文，<br>
帮助学生 **选题、读文献、设计实验、排查论文逻辑、生成代码脚手架、模拟答辩与审稿**。

[安装](#安装) · [使用](#使用) · [核心功能](#核心功能) · [项目结构](#项目结构) · [English](README_EN.md)

</div>

---

## 这是什么

这是一个运行在 Agent Skills / Claude Code 风格目录下的 **meta-skill**。

你给它一位教授的公开材料或授权材料，例如：
- 代表论文 PDF
- 个人主页 / 简历 / 研究方向说明
- 讲义、演讲稿、项目申请书、报告
- 你自己整理的“教授画像”和指导偏好
- 学生当前论文、实验计划、代码片段

它会把这些材料蒸馏成三层：

| 层 | 作用 |
|---|---|
| **Research Memory** | 教授的研究主题、方法谱系、代表成果、常用问题框架 |
| **Advising Persona** | 指导风格、审稿倾向、追问习惯、写作偏好、实验要求 |
| **Action Playbook** | 如何带学生做选题、综述、实验设计、代码原型、答辩准备 |

最终生成一个可调用的 **赛博教授 Skill**。

---

## 安装

### Claude Code

> **重要**：Claude Code 从 **git 仓库根目录** 的 `.claude/skills/` 查找 skill。请在正确位置执行。

```bash
# 安装到当前项目
mkdir -p .claude/skills
git clone https://github.com/YOUR_USERNAME/cyber-professor-skill .claude/skills/create-cyber-professor

# 或安装到全局
git clone https://github.com/YOUR_USERNAME/cyber-professor-skill ~/.claude/skills/create-cyber-professor
```

### 依赖（可选）

```bash
pip install -r requirements.txt
```

---

## 使用

在 Claude Code 中输入：

```bash
/create-cyber-professor
```

然后按提示提供：
1. 教授代号 / 姓名简称
2. 学科、方向、院校/实验室（可选）
3. 你希望蒸馏的材料
4. 你希望这个赛博教授承担什么角色

生成后可用：

```bash
/{slug}
```

来调用该赛博教授 Skill。

### 推荐角色模式

在对话里直接说即可：

| 模式 | 用法示例 |
|---|---|
| 导师模式 | “请用导师模式帮我收敛选题” |
| 文献综述模式 | “请按该教授风格帮我梳理这个方向” |
| 实验设计模式 | “请给我一个可执行的消融实验方案” |
| 审稿人模式 | “请像严格审稿人一样挑问题” |
| 代码教练模式 | “请给我一个最小可运行 PyTorch 原型” |
| 答辩模拟模式 | “请扮演答辩主席连续追问” |

### 管理命令

| 命令 | 说明 |
|---|---|
| `/list-professors` | 列出已生成的赛博教授 |
| `/{slug}` | 调用该赛博教授 |
| `/cyber-professor-rollback {slug} {version}` | 回滚历史版本 |
| `/delete-cyber-professor {slug}` | 删除 |

---

## 核心功能

### 1. 教授研究蒸馏

从论文、主页、讲义、报告中提取：
- 核心研究问题
- 方法论偏好
- 评价创新性的标准
- 实验设计的常用套路
- 写作结构与论证风格
- 可能的学术“雷区”与审稿口味

### 2. 学生课题指导

可以围绕学生当前任务给建议：
- 题目是否收敛
- 创新点是否成立
- 方法设计是否自洽
- 实验设置是否充分
- 论文结构是否清楚
- 哪些结论容易被审稿人攻击

### 3. 实验设计与排错

不仅给“想法”，还要给落地路线：
- baseline 选择
- ablation 设计
- metrics 选择
- 数据划分与公平性检查
- 错误分析框架
- 负结果后的迭代路线

### 4. 代码原型与模型脚手架

可以输出：
- 最小可运行实验框架
- PyTorch / Python 代码骨架
- 配置文件模板
- 数据处理 pipeline 草图
- 训练 / 验证 / 记录规范

> 注意：代码生成属于“科研辅助”，仍需人工检查与复现实验结果。

### 5. 赛博教授可扩展功能

除了“指导论文”，还可以继续发散：

- **选题雷达**：从当前兴趣出发给出 3–5 条可投稿路线
- **研究谱系图**：把某教授近年工作拆成时间线和方法树
- **开题答辩官**：模拟开题、预答辩、组会追问
- **反方审稿人**：专门找漏洞、找不严谨点、找因果跳跃
- **投稿策略助手**：按方向匹配期刊/会议口味与风险
- **学生训练官**：按周布置读论文、复现实验、做笔记任务
- **科研写作教练**：按该教授风格改摘要、引言、贡献、discussion
- **科研军团**：一个教授 + 一个严格审稿人 + 一个代码教练 + 一个文献秘书，组成多 Agent 导师组

---

## 推荐输入材料

### 高优先级
- 代表论文 5–20 篇
- 个人主页 / Google Scholar / DBLP / 实验室主页导出的文字材料
- 研究计划书 / 讲义 / keynote / 访谈
- 你自己写的一份“教授画像”

### 中优先级
- 学生当前论文草稿
- 代码仓库 README / 核心模块
- 实验日志、报错、失败记录

### 低优先级
- 零碎截图
- 缺乏来源的二手介绍文章

---

## 输出结果

每个赛博教授 Skill 默认包含：

| 文件 | 作用 |
|---|---|
| `research_memory.md` | 研究问题、代表成果、方法谱系、术语体系 |
| `advising_persona.md` | 指导风格、批评方式、写作口味、审稿标准 |
| `playbook.md` | 选题/综述/实验/写作/答辩/代码生成流程 |
| `meta.json` | 基本元信息 |
| `SKILL.md` | 最终可运行 Skill |

---

## 项目结构

```text
create-cyber-professor/
├── SKILL.md
├── prompts/
│   ├── intake.md
│   ├── research_analyzer.md
│   ├── persona_analyzer.md
│   ├── research_builder.md
│   ├── persona_builder.md
│   ├── playbook_builder.md
│   ├── merger.md
│   └── correction_handler.md
├── tools/
│   ├── wechat_parser.py
│   ├── qq_parser.py
│   ├── social_parser.py
│   ├── photo_analyzer.py
│   ├── skill_writer.py
│   └── version_manager.py
├── professors/
│   └── example_professor/
├── docs/PRD.md
├── requirements.txt
└── LICENSE
```

---

## 注意事项

- 这是 **“教授风格科研智能体”**，不是对真人的法律或伦理替代。
- 建议优先使用公开材料或已授权材料。
- 对教授私人通信、未公开评审意见、学生隐私材料，要注意权限和边界。
- 论文能体现研究风格，但未必足够体现“指导风格”；最好补充讲义、演讲、课程、访谈、你的人工总结。
- 若运行环境支持联网搜索，可将最新论文检索结果作为额外上下文接入；若不支持，请手动提供检索结果。

---

## 致敬 & 参考

本项目在结构设计上参考了开源 Agent Skill 生态中常见的 `SKILL.md + prompts + tools` 组织方式，并吸收了多个公开技能仓库的经验，例如 OpenAI 的 `skills` 仓库、Anthropic 的 `skills` 仓库，以及 SkillHub 等项目的目录与说明组织思路。它们展示了技能包通常由说明文件、提示模板和辅助脚本构成。

特别感谢：
- **[同事.skill](https://github.com/titanwings/colleague-skill)**（by titanwings）— 首创“把人蒸馏成 AI Skill”的双层架构
- **[前任.skill](https://github.com/therealXiaomanChu/ex-partner-skill)**（by therealXiaomanChu）— 将双层架构迁移到亲密关系场景
- **[自己.skill](https://github.com/notdog1998/yourself-skill)**（by notdog1998）— 将视角转向“自我蒸馏”，完善了自我记忆与人格模板
- GPT-5.4
- Claude Code
- VS Code

**欢迎参加数字永生。**

MIT License © [RunqingZhang](https://github.com/Zhrq-vis)
