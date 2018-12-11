<?php

$verbouFileName = 'verbou.json';
$displegerFileName = 'displeger_format.csv';


$ANV_VERB = 0;
$DIAZ_VERB = 1;
$RUMMAD = 2;
$GALLEG = 3;

echo '<html><head><meta charset="UTF-8"><title>Displeger verbou</title></title>';
echo "<body><h1>Displeger verboù</h1>";
echo '<form><p>Enankit ur verb: <input type="text" name="verb"><button>Kas</button></p></form>';


if (key_exists('verb', $_GET)) {

  $verbouFile = file_get_contents($verbouFileName);
  $verbouArray = json_decode($verbouFile, true);
  $verb = $_GET['verb'];
  echo '<h2>'.$verb.'</h2>';
  $handle = fopen($displegerFileName, "r");
  if ($handle) {
      while (($line = fgets($handle)) !== false) {
        if(substr($line, 0, strlen($verb.';')) === $verb.';') {
          $lineData = explode(';', $line);
          $rummad = $lineData[$RUMMAD];
          $diazVerb = $lineData[$DIAZ_VERB];
          $galleg = $lineData[$GALLEG];

          echo '<p>Galleg : '.$galleg.'</p>';
          echo '<h3>Amzer a-vremañ</h3>';
          printAmzer($diazVerb, $verbouArray[$rummad]['bremañ']);
          echo '<h3>Amzer tremenet ledan</h3>';
          printAmzer($diazVerb, $verbouArray[$rummad]['tremenet_ledan']);
          echo '<h3>Amzer tremenet strizh</h3>';
          printAmzer($diazVerb, $verbouArray[$rummad]['tremenet_strizh']);
          echo '<h3>Amzer da zont</h3>';
          printAmzer($diazVerb, $verbouArray[$rummad]['da_zont']);
          echo '<h3>Amzer gallus</h3>';
          printAmzer($diazVerb, $verbouArray[$rummad]['gallus']);
          echo '<h3>Amzer dic\'hallus</h3>';
          printAmzer($diazVerb, $verbouArray[$rummad]['dichallus']);
          echo '<h3>Amzer kadarnaat</h3>';
          printAmzer($diazVerb, $verbouArray[$rummad]['kadarnaat']);
        }
      }

      fclose($handle);
  } else {

  }

}




function printAmzer($diazVerb, $dibennou) {
    $raganviou = ['U1', 'U2', 'U3', 'L1', 'L2', 'L3', 'D '];
    $amzer = '';
    foreach($dibennou as $key=>$dibenn) {
      if(is_array($dibenn)) {
          $amzer .= '<li>'.$raganviou[$key].'. ';

          foreach($dibenn as $k => $dib) {
            $amzer .= $diazVerb.$dib;
            if($k < count($dibenn)) {
              $amzer.= ' pe ';
            }
          }
          $amzer.= '</li>';
      } elseif(is_string($dibenn)) {
        $amzer .= '<li>'.$raganviou[$key].'. '.$diazVerb.$dibenn.'</li>';

      }
    }
    echo $amzer;
}
