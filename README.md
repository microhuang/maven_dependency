自动生成有冲突的依赖包数据，可以直接t复制到pom.xml文件使用

# 使用

python pom.py

# 效果

```
<!-- list -->

<![CDATA[
['antlr', 'antlr', 'jar', '2.7.2', 'compile', 'com.pay.service', 'pay-web', 'war', '1.0.2-SNAPSHOT\n']
['antlr', 'antlr', 'jar', '2.7.7', 'compile', 'com.pay.service', 'pay-api', 'jar', '1.0.2-SNAPSHOT\n']
]]>

<!-- dependencyManagement -->
<dependencyManagement>

<dependency>
            <groupId>antlr</groupId>
            <artifactId>antlr</artifactId>
            <version>2.7.7</version>
            <scope>compile</scope>
</dependency>

</dependencyManagement>

<!-- dependencies -->

<!-- pay-api -->

<dependencies>

<dependency>
            <groupId>antlr</groupId>
            <artifactId>antlr</artifactId>
</dependency>

</dependencies>

<!-- pay-web -->

<dependencies>

<dependency>
            <groupId>antlr</groupId>
            <artifactId>antlr</artifactId>
</dependency>

</dependencies>
```
