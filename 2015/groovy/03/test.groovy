class Foo{
  def deliveredHouses(List input) {
    coordinates(input).unique().size()
  }

  private coordinates(List input){
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
    result
  }

  def roboSanta(List input){
    def even = input.withIndex().collect{ x, index -> index % 2 == 0 ? x : null } - null
    def odd = input.withIndex().collect{ x, index -> index % 2 == 1 ? x : null } - null
    def robot = coordinates(odd)
    def santa = coordinates(even)
    (robot + santa).unique().size()
  }
}

def input = new File("input.txt").text.toList()
// println "The result is: ${new Foo().delivered_houses(input)}"

println new Foo().roboSanta(input)

