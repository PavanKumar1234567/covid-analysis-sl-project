
BEGIN {
	FS=",";
	OFS=","
}

{
	nacount=0;
	for(i=1;i<=NF;i++)
	{
		if( $i == "")
		{
			$i="NA";
			nacount=nacount+1;
		}
	}
	if( nacount <= 50 )
	{
	print $1,$2,$3,$15,$16,$23,$24;
	}
}

END {
	
}
