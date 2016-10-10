自动生成有冲突的依赖包数据，可以直接t复制到pom.xml文件使用

# 使用

python pom.py

# 效果

```
<!-- dependencyManagement -->
<dependencyManagement>

<dependency>
            <groupId>antlr</groupId>
            <artifactId>antlr</artifactId>
            <version>2.7.2</version>
            <scope>compile</scope>
</dependency>

</dependencyManagement>

<!-- dependencies -->

<!-- pay-mailo-api -->

<dependencies>

<dependency>
            <groupId>antlr</groupId>
            <artifactId>antlr</artifactId>
</dependency>

</dependencies>

<!-- pay-mailo-web -->

<dependencies>

<dependency>
            <groupId>antlr</groupId>
            <artifactId>antlr</artifactId>
</dependency>

</dependencies>
```
