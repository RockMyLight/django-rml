
# Grid protocol

Based on proximity values and other beacons we try to align 
devices that are screen pixels into a euclidean grid.

```
{
	'device': 'xzy', // device string ID or IP
	'neighbors': [{
		'id': 'xyz1',
		'distance': 12, // in meters
	},
	{
		'id': 'xyz2',
		'distance': 12, // in meters
	}]
}

```


# DJ protocol

An example of the "DJ" protocol

GET querry:

`http://www.rockmylight.com/api/dj/?id=1234&lat=123124.123123&lon=213123.4232345234`


JSON reply:

```
{
'num_of_clients': 6, // number of connected clients in the grid
'frames': [{
	'timestamp': 1443828473, // milliseconds since Jan 01 1970. (UTC)
	'color': #fff, // new color - RGB value
},
...
]}

```

## URL Example 2

```
http://rockmylight.com/api/dj/1/
```
