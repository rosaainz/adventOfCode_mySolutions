import org.codehaus.groovy.runtime.EncodingGroovyMethods as Hash

secret = "abcdef"
answer = "609043"

println """ 
  ${secret + answer} => MD5: ${Hash.md5(secret + answer)}
  Rosa => MD5: ${Hash.md5('Rosa')}
"""

secret = "pqrstuv"
answer = "1048970"

println """ 
  ${secret + answer} => MD5: ${Hash.md5(secret + answer)}
  Juan => MD5: ${Hash.md5('Juan')}
"""

secret = "bgvyzdsv"

results = []
(10000..999999).each{ n ->
	hash = Hash.md5(secret + n)
	println "${secret + n} => ${hash}"
	if(hash.startsWith("00000"))
		results << [n, hash]
}


println results