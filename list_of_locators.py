# -*- coding: utf-8 -*-

# Каким образом вы контактировали нашего сотрудника?
first_contact = ['//fieldset[1]//label[1]/span[1]',
                 '//fieldset[1]//label[1]/span[1]',
                 '//fieldset[1]//label[1]/span[1]',
                 '//fieldset[1]//label[1]/span[1]']

# Каким образом вы контактировали нашего сотрудника?
how_contact = ['//fieldset[2]/div/div/label[1]/span',
               '//fieldset[2]/div/div/label[2]/span',
               '//fieldset[2]/div/div/label[3]/span',
               '//fieldset[2]/div/div/label[4]/span']
# driver.find_element_by_xpath(random.choice(how_contact)).click()

# Оцените, пожалуйста, Вашу удовлетворенность нашей поддержкой:

# Решение проблемы
problem_solve = ['//div[2]//label[1]/span[1]',
                 '//div[2]//label[2]/span[1]',
                 '//div[2]//label[3]/span[1]']
# driver.find_element_by_xpath(random.choice(problem_solve)).click()

# Качество совета
answer_quality = ['//div[3]/div[2]/div/label/span',
                  '//div[3]/div[2]/div/label[2]/span',
                  '//div[3]/div[2]/div/label[3]/span']

# driver.find_element_by_xpath(random.choice(answer_quality)).click()

# Скорость отзыва по телефону
answer_speed = ['//fieldset[3]//div[4]/div[2]/div/label[1]/span[1]',
                '//fieldset[3]//div[4]/div[2]/div/label[2]/span[1]',
                '//fieldset[3]//div[4]/div[2]/div/label[3]/span[1]']
# driver.find_element_by_xpath(random.choice(answer_speed)).click()

# Профессиональность и презентабельность
prof_present = ['//div[5]/div[2]/div/label[1]/span',
                '//div[5]/div[2]/div/label[2]/span',
                '//div[5]/div[2]/div/label[3]/span']
# driver.find_element_by_xpath(random.choice(prof_present)).click()

# Ясность и наглядность
clear_view = ['//div[6]/div[2]/div/label[1]/span',
              '//div[6]/div[2]/div/label[2]/span',
              '//div[6]/div[2]/div/label[3]/span']
# driver.find_element_by_xpath(random.choice(clear_view)).click()

# Простота контакта со службой поддержки
simple_contact = ['//div[7]/div[2]/div/label[1]/span',
                  '//div[7]/div[2]/div/label[2]/span',
                  '//div[7]/div[2]/div/label[3]/span']
# driver.find_element_by_xpath(random.choice(simple_contact)).click()

# Оцените, пожалуйста, Вашу удовлетворенность основными сервисами:
# Почта mail.fmrest.com
fmrest_mail = ['//fieldset[4]//div[2]/div[2]/div/label[1]/span',
               '//fieldset[4]//div[2]/div[2]/div/label[2]/span',
               '//fieldset[4]//div[2]/div[2]/div/label[3]/span']
# driver.find_element_by_xpath(random.choice(fmrest_mail)).click()

# Сервис удаленных рабочих столов
rdp_service = ['//fieldset[4]//div[3]/div[2]/div/label[1]/span',
               '//fieldset[4]//div[3]/div[2]/div/label[2]/span',
               '//fieldset[4]//div[3]/div[2]/div/label[3]/span']
# driver.find_element_by_xpath(random.choice(rdp_service)).click()

# 1C
One_ass = ['//fieldset[4]//div[4]/div[2]/div/label[1]/span',
           '//fieldset[4]//div[4]/div[2]/div/label[2]/span',
           '//fieldset[4]//div[4]/div[2]/div/label[3]/span']
# driver.find_element_by_xpath(random.choice(One_ass)).click()

# ПО Профит
profit = ['//fieldset[4]//div[5]/div[2]/div/label[1]/span',
          '//fieldset[4]//div[5]/div[2]/div/label[2]/span',
          '//fieldset[4]//div[5]/div[2]/div/label[3]/span']
# driver.find_element_by_xpath(random.choice(profit)).click()

# файвай
wifi = ['//fieldset[4]//div[6]/div[2]/div/label[1]/span',
        '//fieldset[4]//div[6]/div[2]/div/label[2]/span',
        '//fieldset[4]//div[6]/div[2]/div/label[3]/span']
# driver.find_element_by_xpath(random.choice(wifi)).click()

# Подключение к интернету
inet = ['//fieldset[4]//div[7]/div[2]/div/label[1]/span',
        '//fieldset[4]//div[7]/div[2]/div/label[2]/span',
        '//fieldset[4]//div[7]/div[2]/div/label[3]/span']
# driver.find_element_by_xpath(random.choice(inet)).click()

# Как часто Вы контактируете нашу службу поддержки?
how_frequent = ['//fieldset[5]//label[1]/span[1]',
                '//fieldset[5]//label[2]/span[1]',
                '//fieldset[5]//label[3]/span[1]',
                '//fieldset[5]//label[4]/span[1]',
                '//fieldset[5]//label[5]/span[1]']
# driver.find_element_by_xpath(random.choice(how_frequent)).click()

# Оцените, пожалуйста, в какой степени Вы согласны со следующими утверждениями:
# Сотрудник обладал всей нужной информацией
all_info = ['//fieldset[6]//div[2]/div[2]/div/label[1]/span',
            '//fieldset[6]//div[2]/div[2]/div/label[2]/span',
            '//fieldset[6]//div[2]/div[2]/div/label[3]/span']
# driver.find_element_by_xpath(random.choice(all_info)).click()

# Сотрудник обладал всей нужной информацией
patient = ['//fieldset[6]//div[3]/div[2]/div/label[1]/span[1]',
           '//fieldset[6]//div[3]/div[2]/div/label[2]/span',
           '//fieldset[6]//div[3]/div[2]/div/label[3]/span']
# driver.find_element_by_xpath(random.choice(patient)).click()

# Сотрудник обладал энтузиазмом
enthusiasm = ['//fieldset[6]//div[4]/div[2]/div/label[1]/span[1]',
              '//fieldset[6]//div[4]/div[2]/div/label[1]/span[1]',
              '//fieldset[6]//div[4]/div[2]/div/label[3]/span']
# driver.find_element_by_xpath(random.choice(enthusiasm)).click()

# Сотрудник внимательно слушал
listen = ['//fieldset[6]//div[5]/div[2]/div/label[1]/span[1]',
          '//fieldset[6]//div[5]/div[2]/div/label[2]/span[1]',
          '//fieldset[6]//div[5]/div[2]/div/label[3]/span[1]']
# driver.find_element_by_xpath(random.choice(listen)).click()

# Сотрудник был дружелюбный
friendly = ['//fieldset[6]//div[6]/div[2]/div/label[1]/span[1]',
            '//fieldset[6]//div[6]/div[2]/div/label[2]/span[1]',
            '//fieldset[6]//div[6]/div[2]/div/label[3]/span[1]']
# driver.find_element_by_xpath(random.choice(friendly)).click()

# Сотрудник был внимательный
attentively = ['//fieldset[6]//div[7]/div[2]/div/label[1]/span[1]',
               '//fieldset[6]//div[7]/div[2]/div/label[2]/span[1]',
               '//fieldset[6]//div[7]/div[2]/div/label[3]/span[1]']
# driver.find_element_by_xpath(random.choice(attentively)).click()

# Сотрудник был вежливый
vezhlivyy = ['//fieldset[6]//div[8]/div[2]/div/label[1]/span[1]',
             '//fieldset[6]//div[8]/div[2]/div/label[2]/span[1]',
             '//fieldset[6]//div[8]/div[2]/div/label[3]/span[1]']
# driver.find_element_by_xpath(random.choice(vezhlivyy)).click()

# В какой степени Вы в общем довольны нашей поддержкой?
happy = ['//fieldset[7]/div/div/label[1]/span',
         '//fieldset[7]/div/div/label[2]/span',
         '//fieldset[7]/div/div/label[3]/span']
# driver.find_element_by_xpath(random.choice(happy)).click()

# лист всех локаторов по вопросам
listing = [happy, first_contact,
           how_contact,
           problem_solve,
           answer_quality,
           answer_speed,
           prof_present,
           clear_view,
           simple_contact,
           fmrest_mail,
           rdp_service,
           One_ass,
           profit,
           wifi,
           inet,
           how_frequent,
           all_info,
           patient,
           enthusiasm,
           listen,
           friendly,
           attentively,
           vezhlivyy]
