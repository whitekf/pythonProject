import pyautogui
# pyautogui.FAILSAFE = True

def findAndClick():
    while True:
        videoAdCords = pyautogui.locateCenterOnScreen("play.png")
        bannerCords = pyautogui.locateCenterOnScreen("bannerad.png")
        blackBannerCords = pyautogui.locateCenterOnScreen("black banner.png")

        if videoAdCords or bannerCords or blackBannerCords is not None:
            break

        if videoAdCords is not None:
            pyautogui.click(videoAdCords)
        elif bannerCords is not None:
            pyautogui.click(bannerCords)
        if blackBannerCords is not None:
            pyautogui.click(blackBannerCords)

        findAndClick()

findAndClick()

#print(f'Skipping all of the YouTube ads')