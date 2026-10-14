return {
utf8: s => Array.from(unescape(encodeURIComponent(s)), c=>c.charCodeAt(0)),
sha1: data => {
 const a=data.slice(), bit=a.length*8; a.push(128); while(a.length%64!==56)a.push(0); a.push(0,0,0,0,(bit>>>24)&255,(bit>>>16)&255,(bit>>>8)&255,bit&255);
 let h=[0x67452301,0xefcdab89,0x98badcfe,0x10325476,0xc3d2e1f0]; const rot=(n,b)=>(n<<b)|(n>>>(32-b));
 for(let o=0;o<a.length;o+=64){let w=[];for(let i=0;i<16;i++)w[i]=(a[o+i*4]<<24)|(a[o+i*4+1]<<16)|(a[o+i*4+2]<<8)|a[o+i*4+3];for(let i=16;i<80;i++)w[i]=rot(w[i-3]^w[i-8]^w[i-14]^w[i-16],1);
 let [x,y,z,v,t]=h;for(let i=0;i<80;i++){let f,k;if(i<20){f=(y&z)|(~y&v);k=0x5a827999;}else if(i<40){f=y^z^v;k=0x6ed9eba1;}else if(i<60){f=(y&z)|(y&v)|(z&v);k=0x8f1bbcdc;}else{f=y^z^v;k=0xca62c1d6;}const n=(rot(x,5)+f+t+k+w[i])|0;t=v;v=z;z=rot(y,30);y=x;x=n;}[x,y,z,v,t].forEach((n,i)=>h[i]=(h[i]+n)|0);}
 return h.map(n=>(n>>>0).toString(16).padStart(8,'0')).join('');
},
sha256: data => {
 const k=[0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2];
 const a=data.slice(), bit=a.length*8;a.push(128);while(a.length%64!==56)a.push(0);a.push(0,0,0,0,(bit>>>24)&255,(bit>>>16)&255,(bit>>>8)&255,bit&255);
 let h=[0x6a09e667,0xbb67ae85,0x3c6ef372,0xa54ff53a,0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19];const rot=(n,b)=>(n>>>b)|(n<<(32-b));
 for(let o=0;o<a.length;o+=64){let w=[];for(let i=0;i<16;i++)w[i]=(a[o+i*4]<<24)|(a[o+i*4+1]<<16)|(a[o+i*4+2]<<8)|a[o+i*4+3];for(let i=16;i<64;i++){let p=w[i-15],q=w[i-2];w[i]=(w[i-16]+(rot(p,7)^rot(p,18)^(p>>>3))+w[i-7]+(rot(q,17)^rot(q,19)^(q>>>10)))|0;}
 let [x,y,z,v,t,u,f,g]=h;for(let i=0;i<64;i++){const p=(g+(rot(t,6)^rot(t,11)^rot(t,25))+((t&u)^(~t&f))+k[i]+w[i])|0;const q=((rot(x,2)^rot(x,13)^rot(x,22))+((x&y)^(x&z)^(y&z)))|0;g=f;f=u;u=t;t=(v+p)|0;v=z;z=y;y=x;x=(p+q)|0;}[x,y,z,v,t,u,f,g].forEach((n,i)=>h[i]=(h[i]+n)|0);}
 return h.map(n=>(n>>>0).toString(16).padStart(8,'0')).join('');
}
};
