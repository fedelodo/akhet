<?php if (!isset($exception)) {
    die("Not allowed");
} ?>
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Akhet Demo UI</title>
  </head>
  <body>
    <h1><?php echo $exception->getMessage() ?></h1>
    <pre><?php echo $exception->getTraceAsString(); ?></pre>
  </body>
</html>
