import org.codehaus.groovy.runtime.EncodingGroovyMethods as Hash

secret = "abcdef"
answer = "609043"

println """ 
  ${secret + answer} => MD5: ${Hash.md5(secret + answer)}
  Rosa => MD5: ${Hash.md5('Rosa')}
"""