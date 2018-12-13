import java.io.File
import java.nio.charset.Charset

val currentDir = System.getProperty("user.dir")
// val file = File(currentDir,"Original.txt")
val file = File("C:\\Users\\liangd\\Desktop\\Markdwon\\Original.txt")
println(file)
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
        if ("<p>" in line) {
            line = line.replace("<p>", "").replace("</p>", "")
        }
        if ("<a href=\"" in line) {
            line = line.replace("<a href=\"", "[").replace("\" target=\"_blank\" ", "]")
        }
        if ("<a href=\"https://link.jianshu.com?t=" in line) {
            line = line.replace("<a href=\"https://link.jianshu.com?t=", "")
        }
        if ("rel=\"nofollow\">" in line) {
            line = line.replace("rel=\"nofollow\">", "(").replace("</a>", ")")
        }
        if ("<th>" in line) {
            line = line.replace("<th>", "|")
        }
        if ("</thead>" in line) {
            line = line.replace("</thead>", "| -------- | -------- |")
        }
        if ("<td>" in line) {
            line = line.replace("<td>", "|")
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

