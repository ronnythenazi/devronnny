var dirX = 1;
var dirY = -1;

function setRotation(elem, rad)
{
  setInterval(rotatearound(elem,rad), 100);
}

//default clockwise
function rotatearound(elem, rad, radstep = 20)
{
  var currX = getX(elem);
  var currY = getY(elem);
  var nextX = currX + (dirX*radstep);
  if(nextX >= (rad*2) || nextX <= 0)
  {
    dirX*=-1;
  }
  if(currY >=(rad*2) || currY <= 0)
  {
    dirY*=-1;

  }
  newX = currX + (dirX*radstep);
  newY = dirY * Math.sqrt(Math.pow(rad, 2) - Math.pow((newX - rad), 2));
  newY+= 200;
  $(elem).css('left', newX + 'px');
  $(elem).css('top', newY + 'px');
}

function getY(elem)
{
  var y = $(elem).css('top');
  return ftonum(y);
}
function ftonum(snum)
{
  var val = parseInt(snum.replace("px",""));
  return val;
}
function getX(elem)
{
  var x = $(elem).css('left');
  return ftonum(x);
}
/*
function getCirc(rad)
{
  return  Math.PI * 2 * rad;;
}*/
