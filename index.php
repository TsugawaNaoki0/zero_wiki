<!DOCTYPE html>
<html lang="ja">
 <head>
   <meta charset="utf-8">
   <link rel="stylesheet" href="./home.css">
   <title>HallowinGhost</title>
    <link rel="icon" href="ghost.png"><!-- タイトルにアイコンを設定 -->
    <link rel="apple-touch-icon" href="icon.png"><!-- iphone のアイコンを設定 -->
    <meta name="robots" content="noindex">
 </head>
 <body>
   <div id="cursor"></div>
   <div class="main">
     <br>
     <center>
     <h1>観測中</h1>
     <br>
     <br>
       <div class="middle_main">
         <?php
           echo shell_exec("export LANG=ja_JP.UTF-8; python3 zeroWiki.py ");
          ?>
       </div>
     </center>
     <br>
     <br>
     <br>
     <br>
     <br>
     <br>
     <br>
     <br>
     <br>
     <br>
     <br>
     <br>
     <br>
     <br>
     <br>
  </div>
 </body>
</html>
