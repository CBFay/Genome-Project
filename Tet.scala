// Tet Framework in Scala

// One Tet consists of 8-bits, which contain 4 Quaternary values.
// Interpreting bytes as Tet objects is an extremely efficient way... 
// ...to store Nucleotide sequences.

// Python is incable of creating single-byte objects, making it...
// ...less than ideal for efficiently representing and operating on ultra-large data.

// Created 01.03.2018 by CB Fay

class Tet(val tet : Byte) {
    override def toString() : String = {
        var str = ""
        str += ((tet + 128) / 64)
        str += ((tet + 128) / 16 % 4)
        str += ((tet + 128) / 4 % 4)
        str += ((tet + 128) % 4)
        return str
    }
}

object util {
       def TetToByte(tet : String) : Byte = {
        var b : Int = 0
        b += tet(0) * 64
        b += tet(1) * 16
        b += tet(2) * 4
        b += tet(3)
        return (b-128).toByte
    } 
}

object demo {
    def main(args : Array[String]) {
        var mytet = new Tet(-127)
        println(mytet)
        println(util.TetToByte("0231"))
    }
}
