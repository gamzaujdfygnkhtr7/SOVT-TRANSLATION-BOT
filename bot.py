import os
import asyncio
from playwright.async_api import async_playwright


TEXT = os.getenv("TEXT", "Hello")
SOURCE = os.getenv("SOURCE", "en")
TARGET = os.getenv("TARGET", "ar")


async def translate():
    url = (
        f"https://translate.google.com/"
        f"?sl={SOURCE}&tl={TARGET}&op=translate"
    )

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        print("🌐 فتح Google Translate...")
        await page.goto(url, wait_until="domcontentloaded")

        print(f"📝 النص: {TEXT}")

        textarea = page.locator("textarea").first
        await textarea.fill(TEXT)

        await page.wait_for_timeout(3000)

        result = await page.locator(
            '[data-result-index="0"]'
        ).first.text_content()

        print("━━━━━━━━━━━━━━━━━━")
        print("🤖 النتيجة:")
        print(result)
        print("━━━━━━━━━━━━━━━━━━")

        await browser.close()


if __name__ == "__main__":
    asyncio.run(translate())
