from playwright.sync_api import sync_playwright, Browser, BrowserContext, Page


class BrowserManager:
    _playwright = None
    _browser: Browser | None = None
    _context: BrowserContext | None = None

    @classmethod
    def start(cls) -> None:
        if cls._browser is not None:
            return  # already started

        cls._playwright = sync_playwright().start()
        cls._browser = cls._playwright.chromium.launch(
            headless=True,
            args=["--disable-blink-features=AutomationControlled"],
        )
        cls._context = cls._browser.new_context(
            user_agent=(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            ),
            locale="en-US",
        )

    @classmethod
    def new_page(cls) -> Page:
        if cls._context is None:
            raise RuntimeError("BrowserManager not started")
        return cls._context.new_page()

    @classmethod
    def shutdown(cls) -> None:
        if cls._browser:
            cls._browser.close()
        if cls._playwright:
            cls._playwright.stop()

        cls._browser = None
        cls._context = None
        cls._playwright = None
