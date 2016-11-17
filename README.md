自动生成有冲突的依赖包数据，可以方便直接复制到pom.xml文件使用

#POM依赖管理的原则：

子模块只声明直接依赖包，总模块使用dependencyManagement对所有（存在冲突的）包进行统一声明，并通过properties定义版本值。

# 环境

Linux|MacOS & shell & python2.7+(os&sys&re)

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
