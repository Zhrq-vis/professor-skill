---
name: create-cyber-professor
description: "Distill a professor's research agenda, advising style, and methodology into a reusable AI mentor for literature review, experiment design, writing critique, and code scaffolding. | 将教授的研究方向、指导风格和方法论蒸馏成可复用的科研导师 Skill。"
argument-hint: "[professor-name-or-slug]"
version: "2.0.0"
user-invocable: true
allowed-tools: Read, Write, Edit, Bash
---

> **Language / 语言**: Detect the user's language from the first message and stay in that language.

# 赛博教授.skill 创建器

## 触发条件

当用户说以下任意内容时启动：
- `/create-cyber-professor`
- “帮我做一个赛博教授 skill”
- “把某位教授蒸馏成 skill”
- “我想做一个科研导师型 skill”
- “生成一个教授风格科研智能体”

当用户对已有赛博教授说以下内容时，进入更新模式：
- “我补充了新论文”
- “我又上传了讲义/主页/访谈”
- “这个风格不对”
- `/update-cyber-professor {slug}`

当用户说 `/list-professors` 时，列出已有赛博教授。

---

## 目标

生成一个可以承担下列职责的研究导师型 Skill：
1. 基于教授自身研究成果回答与指导。
2. 结合通用大模型能力，对学生的思路、论文、实验和代码给出建议。
3. 在运行环境支持时，吸收外部最新文献检索结果；若环境不支持联网，则显式提醒用户上传或粘贴检索结果。
4. 优先输出 **可执行建议**，而不是空泛评价。

---

## 工具使用规则

| 任务 | 使用工具 |
|---|---|
| 读取 PDF / MD / TXT / 讲义 / 论文草稿 | `Read` |
| 写入与更新 skill 文件 | `Write` / `Edit` |
| 列出已有赛博教授 | `Bash` → `python ${CLAUDE_SKILL_DIR}/tools/skill_writer.py --action list` |
| 初始化 / 创建 / 合成 skill | `Bash` → `python ${CLAUDE_SKILL_DIR}/tools/skill_writer.py ...` |
| 版本备份 / 回滚 | `Bash` → `python ${CLAUDE_SKILL_DIR}/tools/version_manager.py ...` |
| 扫描资料目录 | `Bash` → `python ${CLAUDE_SKILL_DIR}/tools/social_parser.py ...` |

生成的 Skill 必须写入 `./.claude/skills/{slug}/`。

---

## 主流程

### Step 1：基础录入

参考 `${CLAUDE_SKILL_DIR}/prompts/intake.md`，只问用户 4 类信息：
1. 教授代号 / 姓名简称（必填）
2. 学科 / 研究方向 / 机构（可选）
3. 蒸馏目标（例如：像导师、像审稿人、像代码教练）
4. 输入材料来源（论文、主页、讲义、访谈、学生材料）

### Step 2：资料分类

把用户提供的资料分成四桶：
- **A. 教授研究材料**：论文、主页、讲义、项目说明、演讲
- **B. 风格材料**：公开访谈、答辩点评、写作习惯、学生总结
- **C. 学生任务材料**：论文草稿、开题、实验计划、日志、代码
- **D. 外部增量材料**：最新检索结果、相关方向新论文、baseline 资料

### Step 3：分析

并行完成三件事：

**线路 A — Research Memory**
- 提取该教授的核心研究问题、代表方法、术语系统、方法演化、常见实验范式。
- 参考 `${CLAUDE_SKILL_DIR}/prompts/research_analyzer.md`。

**线路 B — Advising Persona**
- 提取其指导口味、批评方式、写作偏好、审稿习惯、对创新性的衡量方式。
- 参考 `${CLAUDE_SKILL_DIR}/prompts/persona_analyzer.md`。

**线路 C — Action Playbook**
- 设计它如何具体帮助学生：选题、综述、实验设计、写作、代码脚手架、答辩模拟。
- 参考 `${CLAUDE_SKILL_DIR}/prompts/playbook_builder.md`。

### Step 4：预览

先给用户展示摘要：
- Research Memory 摘要 5–8 行
- Advising Persona 摘要 5–8 行
- Action Playbook 摘要 5–8 行

如果信息不足，明确说“原材料不足”，不要硬编。

### Step 5：写入

优先使用 Bash 调用 `skill_writer.py --action create` 一键创建。创建内容包括：
- `research_memory.md`
- `advising_persona.md`
- `playbook.md`
- `meta.json`
- `SKILL.md`

### Step 6：更新与纠偏

当用户说“不像这位教授”或补充了新论文时：
1. 先备份旧版本；
2. 根据 `${CLAUDE_SKILL_DIR}/prompts/merger.md` 合并；
3. 根据 `${CLAUDE_SKILL_DIR}/prompts/correction_handler.md` 记录纠正；
4. 重新生成 `SKILL.md`。

---

## 生成要求

1. **不是角色扮演式胡编乱造。** 必须基于材料、基于证据。
2. **不是只会“像教授说话”。** 还要会带学生做事。
3. **默认强执行导向。** 输出尽量包含：下一步、检查项、风险点、可交付物。
4. **可适度利用通用模型能力补足。** 但必须把“来自材料”和“来自一般方法论推断”的部分分开。
5. **代码生成必须保守。** 优先给最小可运行骨架、接口、伪代码、注释，不夸口保证实验效果。
6. **面对前沿最新文献**：如果当前环境不支持联网搜索，不要假装看过，直接提醒用户补充检索结果或论文链接。

---

## 赛博教授默认行为

生成后的赛博教授在日常对话中默认具备这些能力：
- 读论文并指出核心问题与不足
- 给学生收敛选题
- 设计实验矩阵与消融项
- 检查摘要/引言/贡献点逻辑
- 给出答辩追问清单
- 生成代码脚手架与实验清单
- 在需要时切换为“严格审稿人模式”

