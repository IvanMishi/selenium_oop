Selenium библиотека подключение к JAVA

Версия драйвера и версия selenium должны быть корректны
https://sites.google.com/chromium.org/driver/?pli=1
браузер откроется если 
selenium нашел драйвер на компьютере
корневая папка=new Directory=drivers=положить в нее драйвер браузера
этот фаил нужно указать в системном свойстве 


<dependency>
<groupId>org.seleniumhq.selenium</groupId>
<artifactId>selenium-java</artifactId>
<version>4.8.1</version>
</dependency>
       
