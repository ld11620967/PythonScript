import java.io.File
import java.nio.charset.Charset

val currentDir = System.getProperty("user.dir")
val file = File(currentDir,"Original_CSDN.txt")

val outFile = File(currentDir, "Markdown.txt")
outFile.delete()
var erase = false

file.forEachLine(Charset.forName("GBK")) {
    if (it.contains("</path></svg>")) {
        erase = true
    } else if (it.contains("rel=\"stylesheet\">")) {
        erase = false
    } else if (erase) {
        var line = it

//        if ("<img src=\"" in line) {
//            val r1 = Regex("\\?(.*?)alt=")
//            line = line.replace(r1, "\" alt=")
//        }

        outFile.appendText(line + "\r\n")
    }
}