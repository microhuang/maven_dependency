import os,sys
import re

os.system('sh /tmp/pom.sh')

pattern = re.compile(r'maven-dependency-plugin:2.1:tree')
pom = ''
search = False
file = open('/tmp/pom.tmp','w')
for line in open('/tmp/pom.txt').readlines():
  line = line.lstrip('[WARNING]').lstrip('[INFO]')
  line = line.lstrip(' ').strip('\n')
  if pom and (line.startswith('+') or line.startswith('\\') or line.startswith('|')):
    #print("a"+line+"b")
    line = line.lstrip('+\\|- ') + ':' + pom + '\n'
    file.write(line)
  elif pattern.search(line):
      search = True
  elif search==True:
      search = False
      pom = line
file.close()

os.system('cat /tmp/pom.tmp | sort > /tmp/pom.xml')

dependencyManagement = []
dependencies = {}
cur = []
print("<!-- list -->")
print("\n")
print("<![CDATA[ ")
print("\n")
for line in open('/tmp/pom.xml').readlines():
  line = line.split(":")
  if cur==[] or cur[0][0]==line[0] and cur[0][1]==line[1] and cur[0][2]==line[2]:
      cur.append(line)
  else:
      if len(cur)>1 and cur[0][3]!=cur[len(cur)-1][3]:
        #print("<!-- list --")
        for l in cur:
          print(l)
          if not l[6] in dependencies:
            dependencies[l[6]] = []
          dependencies[l[6]].append("""
<dependency>
            <groupId>%(g)s</groupId>
            <artifactId>%(a)s</artifactId>
</dependency>
""" % {'g':cur[0][0],'a':cur[0][1]})
        dependencyManagement.append("""
<dependency>
            <groupId>%(g)s</groupId>
            <artifactId>%(a)s</artifactId>
            <version>%(v)s</version>
            <scope>%(s)s</scope>
</dependency>
""" % {'g':cur[0][0],'a':cur[0][1],'v':cur[len(cur)-1][3],'s':cur[0][4]})
#        print("""
#<dependency>
#            <groupId>%(g)s</groupId>
#            <artifactId>%(a)s</artifactId>
#            <version>%(v)s</version>
#</dependency>
#""" % {'g':cur[0][0],'a':cur[0][1],'v':cur[0][3]})
        #print("-- list -->")
        print("\n")
      cur = []
      cur.append(line)
print("]]>")
print("\n")

print("<!-- dependencyManagement -->")
print("<dependencyManagement>")
print("<dependencies>")
for l in dependencyManagement:
  print(l)
print("</dependencies>")
print("</dependencyManagement>")

print("\n<!-- dependencies -->\n")

for k,v in dependencies.items():
  print("<!-- %s -->" % (k))
  print("<dependencies>")
  for l in v:
    print(l)
  print("</dependencies>")
