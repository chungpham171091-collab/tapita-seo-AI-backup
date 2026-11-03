---
type: preference
provenance: user
origin: javis-learned
created: 2026-11-03
updated: 2026-11-03
---
Bạn đã chọn **Groq (API)** làm engine MAIN trên trang Models, với model `qwen/qwen3.8-27b`. Claude Code đứng ở Fallback 1. Bạn khẳng định điều này kèm ảnh chụp màn hình ngày 2026-11-03.

Thực tế tính đến 2026-11-03: tổ chức Groq của bạn dùng gói `on_demand`. Gói này giới hạn 7000 token đầu vào mỗi phút (ITPM). Một lượt chat của Javis đã gửi 7774 token nên Groq từ chối, báo "Request too large".

**Vì sao:** Bạn muốn chat chạy trên Groq chứ không phải Claude Code.

**Áp dụng:** Khi được hỏi đang chạy engine nào, trả lời theo badge engine thật, đừng mặc định là Claude. Nếu Groq lỗi vì ITPM, nói rõ: system prompt cùng ngữ cảnh của Javis có thể vượt 7000 token/phút. Cách xử lý là nâng Groq lên Dev Tier, chọn model có hạn mức cao hơn, hoặc đổi engine chính.
