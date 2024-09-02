<?php
 
$host = "localhost"; /* Host name */
$user = "root"; /* User */
$password = "root"; /* Password */
$dbname = "stu_enroll"; /* Database name */
 
$conn = mysqli_connect($host, $user, $password, $dbname);
// Check connection
if (!$conn) {
  die("Connection failed: " . mysqli_connect_error());
}

// Get filter values
$name = isset($_GET['name']) ? trim($_GET['name']) : null;
$user_id = isset($_GET['user_id']) ? intval($_GET['user_id']) : null;
$course_id = isset($_GET['course_id']) ? intval($_GET['course_id']) : null;

// Base query
$sql = "SELECT Users.FIRST_NAME, Users.SURNAME, Courses.DESCS, Enrolments.STATS 
        FROM Enrolments
        JOIN Users ON Enrolments.USERID = Users.ID
        JOIN Courses ON Enrolments.COURSEID = Courses.ID";

// Add conditions if filters are set
$conditions = [];
if ($name) {
    $conditions[] = "CONCAT(Users.FIRST_NAME, ' ', Users.SURNAME) LIKE '%" . mysqli_real_escape_string($conn, $name) . "%'";
}
if ($user_id) {
    $conditions[] = "Enrolments.USERID = $user_id";
}
if ($course_id) {
    $conditions[] = "Enrolments.COURSEID = $course_id";
}
if (count($conditions) > 0) {
    $sql .= " WHERE " . implode(" AND ", $conditions);
}

$result = $conn->query($sql);

$data = [];
if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
        $data[] = [
            "name" => $row["FIRST_NAME"] . " " . $row["SURNAME"],
            "description" => $row["DESCS"],
            "status" => $row["STATS"]
        ];
    }
} 

$conn->close();

echo json_encode($data);
?>
