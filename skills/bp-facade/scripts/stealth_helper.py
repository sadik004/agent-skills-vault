"""
Universal Stealth Helper for Multi-Project Automation
Supports Playwright, Patchright, Undetected-ChromeDriver, Selenium, and Pyppeteer.
"""
from pathlib import Path
from typing import Any

STEALTH_JS_PATH = Path(__file__).parent / "stealth_evasion.js"

def get_stealth_js() -> str:
    """Returns the raw JavaScript payload containing all active evasion layers."""
    if STEALTH_JS_PATH.exists():
        return STEALTH_JS_PATH.read_text(encoding="utf-8")
    return ""

async def apply_stealth_playwright(page_or_context: Any) -> None:
    """
    Applies all stealth evasion layers to a Playwright/Patchright Page or BrowserContext.
    Executes before ANY site script runs.
    
    Usage:
        await apply_stealth_playwright(page)
        # or
        await apply_stealth_playwright(context)
    """
    js_payload = get_stealth_js()
    if hasattr(page_or_context, "add_init_script"):
        await page_or_context.add_init_script(js_payload)

def apply_stealth_selenium(driver: Any) -> None:
    """
    Applies stealth evasion layers to Selenium or Undetected-ChromeDriver (uc) via CDP.
    
    Usage:
        apply_stealth_selenium(driver)
    """
    js_payload = get_stealth_js()
    if hasattr(driver, "execute_cdp_cmd"):
        driver.execute_cdp_cmd(
            "Page.addScriptToEvaluateOnNewDocument",
            {"source": js_payload}
        )
