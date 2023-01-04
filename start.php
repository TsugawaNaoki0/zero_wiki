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
     <h1><font color="white">zeroWiki STARTED</font></h1>
     <form  action="" method="post" class="login">
       <input type="hidden" class="login" name="url_reg" value="<?php echo $_POST["url_start"]; ?>">
     </form>
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


<?php
  echo shell_exec("export LANG=ja_JP.UTF-8; while true; do python3 zeroWiki.py ".$_POST["url_start"]." sleep 3s; done");
?>
