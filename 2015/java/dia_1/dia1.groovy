file = new File("/Users/rosasainz/Documents/prog/rosa/versionado/adventOfCode_mySolutions/2015/java/dia_1/input.txt")
println file.getClass()

text = file.text
println text.getClass()
floor = 0
for(int i=0; i < text.size(); i++){
	char c = text[i];
	if( c == '(' ){
		floor += 1;
	} else if(c == ')') {
		floor -= 1;
	}
}
println floor
