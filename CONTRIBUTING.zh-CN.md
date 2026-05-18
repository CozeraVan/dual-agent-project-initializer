# 贡献指南

感谢你关注 Dual Agent Project Initializer。

## 开发环境

```bash
python -m pip install -e .[dev]
ruff check .
pytest -q
python scripts/compile_release.py
```

## 如何修改模板

模板文件位于：

```text
src/dual_agent_initializer/templates/
```

不要直接修改生成的 `dist/init-agent-project.py`。它由以下命令生成：

```bash
python scripts/compile_release.py
```

## PR 检查清单

- 不要把短期 `12_AGENT_BOARD.md` 内容和长期 workflow 规则混在一起。
- 如果修改 workflow 规则，请同步检查 `AGENTS.md`、`CLAUDE.md`、`02_LOCKED_REQUIREMENTS.md`、`11_AGENT_STATE.md`、`13_CHANGE_CONTROL.md` 是否需要更新。
- 运行测试并重新生成 release 脚本。
- 不要提交 `.env`、token、密钥或真实私有项目数据。

## 推荐贡献方向

- 更多项目类型模板；
- 更好的 Change Request 流程；
- 更强的检查脚本；
- 示例项目；
- 适配更多 Agent；
- 文档翻译。
