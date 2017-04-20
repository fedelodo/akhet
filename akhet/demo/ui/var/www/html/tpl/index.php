<?php if (!isset($images) || !isset($shared_instances)) {
    die("Not allowed");
} ?>
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Akhet Demo UI</title>
  </head>
  <body>
    <h1>Images</h1>
      <?php
      foreach ($images as $image) {
          $prefix = "akhet/images/";
          if (substr($image, 0, strlen($prefix))==$prefix) {
              ?>

      <form action="/" method="post">
        <label><?php echo substr($image, strlen($prefix)); ?></label>
        <input type="hidden" name="instance_image" value="<?php echo $image; ?>" />
        <input type="submit" value="Run!" />
      </form>

          <?php

          }
      }
      ?>

    <h1>Shared instances</h1>
    <ul>
      <?php
      foreach ($shared_instances as $id => $link) {
          ?>

      <li><a href="<?php echo $link; ?>"><?php echo $id; ?></a></li>

        <?php

      }
      ?>
    </ul>
  </body>
</html>
