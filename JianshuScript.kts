import java.io.File
import java.nio.charset.Charset

val currentDir = System.getProperty("user.dir")
val file = File(currentDir, "Original.txt")
//val contents = file.readText(Charset.forName("GBK"))
// println(contents)

val outFile = File(currentDir, "Markdown.txt")
outFile.delete()
var erase = false

file.forEachLine(Charset.forName("GBK")) {
    if (it.contains("<article class=\"_2rhmJa\"")) {
        erase = true
    } else if (it.contains("</article>")) {
        erase = false
    } else if (erase) {
        var line = it
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
        if ("https://link.jianshu.com?t=" in line) {
            line = line.replace("https://link.jianshu.com?t=", "")
        }
        if ("links.jianshu.com/go?to=https%3A%2F%2F" in line) {
            line = line.replace("links.jianshu.com/go?to=https%3A%2F%2F", "")
            line = line.replace("%2F", "/")           
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
            line = line.replace(r1, "![](").replace(r2, ")")
        }
        if ("</p>" in line) {
            line = line.replace("</p>", "\r\n")
        }
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
        if ("<td>" in it) {
            outFile.appendText(it)
        }
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

        if (")[" in line && "(" in line && "]" in line) {
            val r1=Regex("^(.*?)\\(")
            val r2=Regex("\\((.*?)\\)")
            val r3=Regex("\\[(.*?)\\]")
            val r4=Regex("\\](.*?)$")
            val line1 = r1.find(line)!!.value
            val line2 = r2.find(line)!!.value
            val line3 = r3.find(line)!!.value
            val line4 = r4.find(line)!!.value
            line=line1.substring(0,line1.length-1)+line3+line2+line4.substring(1,line4.length)
        }
        outFile.appendText(line + "\r\n")
    }
}