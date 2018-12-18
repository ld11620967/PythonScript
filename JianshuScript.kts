import java.io.File
import java.nio.charset.Charset

val currentDir = System.getProperty("user.dir")
val file = File(currentDir,"Original_Jianshu.txt")
//val contents = file.readText(Charset.forName("GBK"))
// println(contents)

val outFile = File(currentDir, "Markdown.txt")
outFile.delete()
var erase = false

file.forEachLine(Charset.forName("GBK")) {
    if (it.contains("<div class=\"show-content-free\">")) {
        erase = true
    } else if (it.contains("<!-- 连载目录项 -->")) {
        erase = false
    } else if (erase) {
        var line = it
        if ("            <p>" in line) {
            line = line.replace("            <p>", "")
        }
        if ("<h1>" in line) {
            line = line.replace("<h1>", "## ").replace("</h1>", "")
        }
        if ("<h2>" in line) {
            line = line.replace("<h2>", "## ").replace("</h2>", "")
        }
        if ("<h3>" in line) {
            line = line.replace("<h3>", "### ").replace("</h3>", "")
        }
        if ("<h4>" in line) {
            line = line.replace("<h4>", "### ").replace("</h4>", "")
        }
        if ("<h5>" in line) {
            line = line.replace("<h5>", "#### ").replace("</h5>", "")
        }
        if ("<h6>" in line) {
            line = line.replace("<h6>", "#### ").replace("</h6>", "")
        }
        if ("<pre><code class=\"java\">" in line) {
            line = line.replace("<pre><code class=\"java\">", "```java\n")
        }
        if ("<pre><code class=\"xml\">" in line) {
            line = line.replace("<pre><code class=\"xml\">", "```xml\n")
        }
        if ("<pre><code class=\"groovy\">" in line) {
            line = line.replace("<pre><code class=\"groovy\">", "```\n")
        }
        if ("<pre><code>" in line) {
            line = line.replace("<pre><code>", "```\n")
        }
        if ("<code>" in line) {
            line = line.replace("<code>", "```")
        }
        if ("</code></pre>" in line) {
            line = line.replace("</code></pre>", "```\n")
        }
        if ("</code>" in line) {
            line = line.replace("</code>", "```")
        }
        if ("<a href=\"" in line) {
            line = line.replace("<a href=\"", "(").replace("\" target=\"_blank\" ", ")")
        }
        if ("<a href=\"https://link.jianshu.com?t=" in line) {
            line = line.replace("<a href=\"https://link.jianshu.com?t=", "")
        }
        if ("rel=\"nofollow\">" in line) {
            line = line.replace("rel=\"nofollow\">", "[").replace("</a>", "]")
        }
        if ("<li>" in line) {
            line = line.replace("<li>", "- ")
        }
        if ("<strong>" in line) {
            line = line.replace("<strong>", "**").replace("</strong>", "**")
        }
        if ("<em>" in line) {
            line = line.replace("<em>", "*").replace("</em>", "*")
        }
        if ("<img" in line) {
            val r1 = Regex("^<div(.*?)<img data-original-src=\"")
            val r2 = Regex("\" data-original-width(.*?)\"></div>")
            line = line.replace(r1, "![Picture](").replace(r2, ")")
        }
        if ("</p>" in line) {
            line = line.replace("</p>", "\r\n")
        }


//        if ("<th>" in line) {
//            line = line.replace("<th>", "|")
//        }
//        if ("</thead>" in line) {
//            line = line.replace("</thead>", "| -------- | -------- |")
//        }
//        if ("<td>" in line) {
//            line = line.replace("<td>", "|")
//        }


        if ("<table>" in it) {
            outFile.appendText(it)
        }
        if ("</table>" in it) {
            outFile.appendText(it)
        }
        if ("<thead>" in it) {
            outFile.appendText(it)
        }
        if ("</thead>" in it) {
            outFile.appendText(it)
        }
        if ("<tr>" in it) {
            outFile.appendText(it)
        }
        if ("</tr>" in it) {
            outFile.appendText(it)
        }
        if ("<th>" in it) {
            outFile.appendText(it)
        }
//        if ("</th>" in it) {
//            outFile.appendText(it)
//        }
        if ("<td>" in it) {
            outFile.appendText(it)
        }
//        if ("</td>" in it) {
//            outFile.appendText(it)
//        }
        if ("<tbody>" in it) {
            outFile.appendText(it)
        }
        if ("</tbody>" in it) {
            outFile.appendText(it)
        }


        val r1 = Regex("<[^>]+>(.*)</[^>]+>", RegexOption.CANON_EQ)
        val r2 = Regex("<[^>]+>", RegexOption.CANON_EQ)
        line = line.replace(r1, "").replace(r2, "")

        if ("&lt;" in line) {
            line = line.replace("&lt;", "<")
        }
        if ("&gt;" in line) {
            line = line.replace("&gt;", ">")
        }
        outFile.appendText(line + "\r\n")
    }
}



//fun exchange(target: String, pos1: Int, pos2: Int): String {
//    var pos1 = pos1
//    var pos2 = pos2
//    if (pos2 < pos1) {
//        val temp = pos2
//        pos2 = pos1
//        pos1 = temp
//    }
//    if (pos1 == pos2 || pos2 >= target.length || pos1 <= -1) {
//        return target
//    }
//    val str1 = target.substring(pos1, pos1 + 1)
//    val str2 = target.substring(pos2, pos2 + 1)
//    val buf = StringBuffer(target.length)
//    return buf.append(target.substring(0, pos1)).append(str2)
//        .append(target.substring(pos1 + 1, pos2)).append(str1)
//        .append(target.substring(pos2 + 1)).toString()
//}