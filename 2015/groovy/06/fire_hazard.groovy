class FireHazard {
  List range(Map c1, Map c2){
    (c1.x..c2.x).collectMany { x -> (c1.y..c2.y).collect { y -> [x,y] } }
  }
}

def c1 = [x:0, y:0]
def c2 = [x:2, y:2]

def range = new FireHazard().range(c1,c2)

println range

