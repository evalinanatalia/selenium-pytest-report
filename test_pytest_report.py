import pytest, unittest, datetime
from selenium import webdriver
import sys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
import time

def test_a_success_login(browser): 

    driver = browser

    driver.get("http://barru.pythonanywhere.com/daftar")
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div[2]/form/input[1]").send_keys('jagoqaindonesia@gmail.com')
    time.sleep(1)
    driver.find_element_by_id("password").send_keys('sman60jakarta')
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div/div[2]/form/input[3]').click()
    time.sleep(2)

    respon_welcome = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/h2').text
    respon_berhasil = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]').text

    assert respon_welcome == 'Welcome Jago QA'
    assert respon_berhasil == 'Anda Berhasil Login'

def test_b_failed_login_email_not_registered(browser): 

    driver = browser 

    driver.get("http://barru.pythonanywhere.com/daftar")
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div[2]/form/input[1]").send_keys('tester.ganteng@jumawa.com')
    time.sleep(1)
    driver.find_element_by_id("password").send_keys('sman60jakarta')
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div/div[2]/form/input[3]').click()
    time.sleep(2)

    respon_welcome = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/h2').text
    respon_berhasil = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]').text

    assert respon_welcome== "User's not found"
    assert respon_berhasil== 'Email atau Password Anda Salah'

def test_c_failed_login_with_invalid_email_valid_password(browser): 

    driver = browser 

    driver.get("http://barru.pythonanywhere.com/daftar")
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div[2]/form/input[1]").send_keys('barru.kurniawan')
    time.sleep(1)
    driver.find_element_by_id("password").send_keys('sman60jakarta')
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div/div[2]/form/input[3]').click()
    time.sleep(2)

    respon_error_email = driver.find_element_by_xpath("/html/body/div/div[2]/form/input[1]").get_attribute("validationMessage")

    assert "Please include an '@' in the email address. 'barru.kurniawan' is missing an '@'."== respon_error_email

def test_d_failed_login_email_with_random_email_valid_password(browser): 

    driver = browser 

    driver.get("http://barru.pythonanywhere.com/daftar")
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div[2]/form/input[1]").send_keys('barru.asdajsdasdasd@bkabka.com')
    time.sleep(1)
    driver.find_element_by_id("password").send_keys('sman60jakarta')
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div/div[2]/form/input[3]').click()
    time.sleep(2)

    respon_welcome = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/h2').text
    respon_berhasil = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]').text

    assert respon_welcome == "User's not found"
    assert respon_berhasil == 'Email atau Password Anda Salah'

def test_e_failed_login_with_phone_number_valid_password(browser): 

    driver = browser 

    driver.get("http://barru.pythonanywhere.com/daftar")
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div[2]/form/input[1]").send_keys('088823772363')
    time.sleep(1)
    driver.find_element_by_id("password").send_keys('sman60jakarta')
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div/div[2]/form/input[3]').click()
    time.sleep(2)

    respon_error_email = driver.find_element_by_xpath("/html/body/div/div[2]/form/input[1]").get_attribute("validationMessage")

    assert "Please include an '@' in the email address. '088823772363' is missing an '@'."== respon_error_email

def test_f_failed_login_with_username_valid_password(browser): 

    driver = browser 

    driver.get("http://barru.pythonanywhere.com/daftar")
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div[2]/form/input[1]").send_keys('barrukurniawan')
    time.sleep(1)
    driver.find_element_by_id("password").send_keys('sman60jakarta')
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div/div[2]/form/input[3]').click()
    time.sleep(2)

    respon_error_email = driver.find_element_by_xpath("/html/body/div/div[2]/form/input[1]").get_attribute("validationMessage")

    assert "Please include an '@' in the email address. 'barrukurniawan' is missing an '@'."== respon_error_email

def test_g_failed_login_empty_email_valid_password(browser): 

    driver = browser 

    driver.get("http://barru.pythonanywhere.com/daftar")
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div[2]/form/input[1]").send_keys('')
    time.sleep(1)
    driver.find_element_by_id("password").send_keys('sman60jakarta')
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div/div[2]/form/input[3]').click()
    time.sleep(2)

    respon_welcome = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/h2').text
    respon_msg = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]').text

    assert respon_welcome== "Email tidak valid"
    assert respon_msg== 'Cek kembali email anda'

def test_h_failed_login_empty_email_empty_password(browser): 

    driver = browser 

    driver.get("http://barru.pythonanywhere.com/daftar")
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div[2]/form/input[1]").send_keys('')
    time.sleep(1)
    driver.find_element_by_id("password").send_keys('')
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div/div[2]/form/input[3]').click()
    time.sleep(2)

    respon_welcome = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/h2').text
    respon_msg = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]').text

    assert respon_welcome== "Email tidak valid"
    assert respon_msg== 'Cek kembali email anda'

def test_k_failed_login_with_max_char_in_email(browser): 

    driver = browser 

    driver.get("http://barru.pythonanywhere.com/daftar")
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div[2]/form/input[1]").send_keys('tester.gantenggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg@jumawa.com')
    time.sleep(1)
    driver.find_element_by_id("password").send_keys('sman60jakarta')
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div/div[2]/form/input[3]').click()
    time.sleep(2)

    respon_welcome = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/h2').text
    respon_berhasil = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]').text

    assert respon_welcome== "Email/Password melebihin maksimal karakter"

def test_l_failed_login_with_max_char_in_password(browser): 

    driver = browser 

    driver.get("http://barru.pythonanywhere.com/daftar")
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div[2]/form/input[1]").send_keys('barru.kurniawan@gmail.com')
    time.sleep(1)
    driver.find_element_by_id("password").send_keys('sman60jakartaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div/div[2]/form/input[3]').click()
    time.sleep(2)

    respon_welcome = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/h2').text
    respon_berhasil = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]').text

    assert respon_welcome== "Email/Password melebihin maksimal karakter"

def test_c_failed_login_with_symbol_validation_in_password(browser): 

    driver = browser

    driver.get("http://barru.pythonanywhere.com/daftar")
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div[2]/form/input[1]").send_keys('tester.ganteng@gmail.com')
    time.sleep(1)
    driver.find_element_by_id("password").send_keys("SELECT%count%(*)%FROM%Users%WHERE%Username='jebol'%or%1=1%--%'%AND%Password=%'email")
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div/div[2]/form/input[3]').click()
    time.sleep(2)

    respon_welcome = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/h2').text
    respon_gagal = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]').text

    assert respon_welcome== "Password tidak valid"
    assert respon_gagal== 'Tidak boleh mengandung symbol'

def test_a_failed_register_with_phone_password_empty(browser): 

    driver = browser 

    driver.get("http://barru.pythonanywhere.com/daftar")
    time.sleep(2)
    driver.find_element_by_id("signUp").click() #tombol sign up disebelah kanan
    time.sleep(2)
    driver.find_element_by_id("email_register").send_keys('0138127391263') #row email
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div/div[1]/form/input[4]').click() #tombol signup untuk daftar
    time.sleep(2)

    error_email = driver.find_element_by_id("email_register").get_attribute("validationMessage")

    assert "Please include an '@' in the email address. '0138127391263' is missing an '@'."== error_email


def test_zona_down(browser):
    browser.close()