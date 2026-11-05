# multi-agent-kit (Tiếng Việt)

Bộ multi-agent dùng lại cho [Claude Code](https://claude.com/claude-code), dành cho dự án **web và mobile**. Cài một lần, dùng cho mọi dự án.

[English](README.md)

## Gồm những gì

- **15 agent:**
  - Lập kế hoạch: `planner`, `architect`.
  - Xây dựng: `coder`, `web-frontend`, `mobile-dev`, `backend-api`, `devops-release`.
  - Kiểm tra: `tester`, `debugger`, `reviewer`, `security-auditor`, `accessibility-auditor`, `performance-optimizer`.
  - Hỗ trợ: `doc-writer`, `researcher`.
- **9 skill:** `/auto` (tự phân tích và chọn luồng), `/feature`, `/bugfix`, `/review`, `/research`, `/init-project`, `tdd`, `mobile-release`, `web-launch-check`.
- **Hook an toàn:** chặn lệnh nguy hiểm (`rm -rf /`, force push, `git reset --hard`, `curl | sh`), chặn sửa file bí mật (`.env`, keystore, chứng chỉ), tự format file vừa sửa bằng formatter của dự án.

## Cài đặt

Cách 1, plugin (khuyên dùng):

```
/plugin marketplace add phamhoang98/repo_agent
/plugin install multi-agent-kit@multi-agent-kit
```

Cách 2, script:

```bash
git clone https://github.com/phamhoang98/repo_agent.git
./repo_agent/scripts/install.sh --profile mobile --with-hooks /duong/dan/du-an
```

Profile: `core`, `web`, `mobile`, `all`. Thêm `--user` để cài cho mọi dự án, `--uninstall` để gỡ, `--dry-run` để xem trước.

## Bắt đầu

1. Trong dự án, chạy `/init-project` để tạo `CLAUDE.md`, rồi điền các mục TODO.
2. Cứ mô tả việc bằng lời thường. Bảng **Agent routing** trong `CLAUDE.md` (do `/init-project` tạo) giúp Claude tự chọn agent phù hợp.
3. Hoặc dùng `/auto <việc cần làm>`: tự phân tích rồi chạy đúng luồng. Muốn ép luồng cụ thể thì dùng:
   - `/feature thêm màn hình đăng nhập cho web và mobile`
   - `/bugfix app crash khi mở cài đặt lúc offline`
   - `/review`
   - `/mobile-release`

Khi cài dạng plugin, tên có tiền tố: `multi-agent-kit:reviewer`, `/multi-agent-kit:feature`.

Xem chi tiết trong [README.md](README.md).
