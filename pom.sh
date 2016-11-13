
pom="pom.xml"
if [ ! -f "$pom" ]; then
  echo "\"$pom\" 不存在，请检查路径是否正确！"
  exit
fi

mvn="/Applications/NetBeans/NetBeans 8.1.app/Contents/Resources/NetBeans/java/maven/bin/mvn"
if [ ! -f "$mvn" ]; then
  echo "\"$mvn\" 不存在，请检查路径是否正确！"
  exit
fi

JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.8.0_91.jdk/Contents/Home "$mvn" dependency:tree -l=/tmp/pom.txt

exit

#JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.8.0_91.jdk/Contents/Home "/Applications/NetBeans/NetBeans 8.1.app/Contents/Resources/NetBeans/java/maven/bin/mvn" dependency:tree -l=/tmp/pom.txt

#exit

#cat /tmp/pom.txt | grep ":jar:" | grep -v -E "^[a-zA-Z]" | sed 's/[^a-zA-Z]*//' | sort | uniq > /tmp/pom.xml

#cat /tmp/pom.txt | grep ":jar:" | grep -v -E "^[a-zA-Z]" | sed 's/[^a-zA-Z]*//' | cut -d: -f 2 | sort | uniq > /tmp/pom.xml

sed -i '' '/[a-zA-Z]/i\
<dependency>
' /tmp/pom.txt

sed -i '' '/[a-zA-Z]/a\
</dependency>
' /tmp/pom.txt

sed -i '' "1 i\
<dependencyManagement><dependencies>
" /tmp/pom.txt

sed -i '' "$ a\
</dependencies></dependencyManagement>
" /tmp/pom.txt
