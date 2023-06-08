import org.codehaus.groovy.runtime.EncodingGroovyMethods as Hash

secret = "bgvyzdsv"

results = []
(10000..999999).each { n ->
	hash = Hash.md5(secret + n)
	if(hash.startsWith("00000"))
		results << [n, hash]
}

println results