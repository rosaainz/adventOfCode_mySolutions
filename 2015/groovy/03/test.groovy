class Foo{
  def delivered_houses(List input) {

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
    result.unique().size()
  }
}

def input = new File("input.txt").text.toList()
println "The result is: ${new Foo().delivered_houses(input)}"
