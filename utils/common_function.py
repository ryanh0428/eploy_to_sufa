def page_toggle(driver) -> None:
    original_tab = driver.current_window_handle
    windows = driver.window_handles
    new_tab = [handle for handle in windows if handle != original_tab][0]
    driver.switch_to.window(new_tab)