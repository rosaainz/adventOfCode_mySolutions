def input = "^>v<".toList()
// def input = "^v^v^v^v^v".toList()

def file = new File("input.txt").text
input = file.toList()


def coor = [0,0]
def result =  input.collect {
  switch(it) {
    case ">":
    coor[0] +=1
    break
    case "<":
    coor[0] -=1
    break
    case "^":
    coor[1] +=1
    break
    case "v":
    coor[1] -=1
    break
  }
  coor.clone()
}
// println result
result << [0,0]
// println result


println result.unique().size()
