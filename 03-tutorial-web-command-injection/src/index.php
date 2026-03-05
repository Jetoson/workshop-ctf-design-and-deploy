<?php
$output = [];
if (isset($_GET['ip'])) {
    // VULNERABILITY: No input validation/sanitization before passing to exec()
    exec("ping -c 1 " . $_GET['ip'], $output);
}
?>
<!DOCTYPE html>
<html>
<head>
    <title>Ping Service</title>
</head>
<body>
    <h1>Network Diagnostics Tool</h1>
    <p>Enter an IP address to ping:</p>
    <form method="GET">
        IP Address: <input type="text" name="ip" placeholder="127.0.0.1">
        <input type="submit" value="Ping">
    </form>

    <?php if (!empty($output)): ?>
    <h2>Results:</h2>
    <pre>
<?php
    foreach ($output as $line) {
        echo htmlspecialchars($line) . "\n";
    }
?>
    </pre>
    <?php endif; ?>
</body>
</html>
