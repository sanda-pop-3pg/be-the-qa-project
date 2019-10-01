import time


def test_ubuntu(driver):
    driver.get('http://ubuntu.com')
    print(driver.title)
    time.sleep(10)
   

def test_redhat(driver):
    driver.get('http://redhat.com')
    print(driver.title)
    time.sleep(10)
