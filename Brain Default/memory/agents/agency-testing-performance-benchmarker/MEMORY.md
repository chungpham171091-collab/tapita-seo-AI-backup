## Bài học (tự học)
- Đo Core Web Vitals lab bằng `npx lighthouse` với CHROME_PATH trỏ tới Chrome local. PSI API dùng key chung hết quota nhanh nên không dựa vào được.
- Site sau Cloudflare trả 429 sau ~20 request (Retry-After 60). Một lần Lighthouse đã đốt hết hạn mức, nên lên kế hoạch đo HTML/headers trước khi chạy Lighthouse, và không dùng Start-Sleep để chờ vì bị chặn.
