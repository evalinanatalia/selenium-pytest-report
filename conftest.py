import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time
import yagmail
import datetime

driver = None

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_")+".png"
            screen_img = _capture_screenshot()
            if file_name:
                # html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:300px;" ' \
                #        'onclick="window.open(this.src)" align="right"/></div>' % screen_img
                # extra.append(pytest_html.extras.html(html))
                now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
                nama_gambar = 'gambar-%s.png' % now
                gambar = driver.get_screenshot_as_file(nama_gambar)
                ofile = os.path.join(os.getcwd(), nama_gambar)

                html = '<div><img src="%s" alt="screenshot" style="width:600px;height:300px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % ofile
                extra.append(pytest_html.extras.html(html))

                send_email = _send_email_report()

        report.extra = extra

def _capture_screenshot():
    '''
         The screenshot is saved as base64 and displayed in html
    :return:
    '''
    return driver.get_screenshot_as_base64()

def _send_email_report():
    file_html = os.path.join(os.getcwd(), "report.html")
    yagmail.register('evalinasimangunsong.es@gmail.com', 'boruhasian')
    yag = yagmail.SMTP('smtp.gmail.com')
    to = 'evasimangunsong0912@gmail.com'
    subject = 'Laporan Testing Login'
    body = 'Hi This is your report'
    yag.send(to = to, subject = subject, contents = body, attachments=file_html)

@pytest.fixture(scope='session', autouse=True)
def browser():
    global driver
    if driver is None:
        driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver
