import React, { useEffect, useRef, useState } from 'react'
import css from '../astylus/chat.module.css'
import { PixelArtCard } from 'react-pixelart-face-card'

function Chat() {
    const [input, setInput] = useState("");
    const [recv, setRecv] = useState([]);
    const [arr, setArr] = useState([]);
    const mssgend = useRef();
    const [slide, setSlide] = useState(false);
    const [activ, setActiv] = useState({ one: true, two: false, three: false });
    const name = localStorage.getItem('name');
    const gen = localStorage.getItem('gen');

    useEffect(() => {               //to automatically scroll down after an input is sent
        mssgend.current?.scrollIntoView({ behavior: "smooth" })
    }, [input])

    function changeInput(e) {
        setInput(e.target.value);
    }

    const send = async (e) => {
        e.preventDefault();
        if (input.trim() !== "") {
            setArr([...arr, input])
            if (activ.one) {
                const res = await fetch("http://localhost:5000/chat", {
                    method: "POST",
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ message: input })
                });
                var temp = await res.json();
                setRecv([...recv, temp.message]);
            }
            else if (activ.two) {
                const res = await fetch("http://localhost:5000/chat", {
                    method: "POST",
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ message: input })
                });
                var temp = await res.json();
                setRecv([...recv, temp.message]);
            }
            else {
                const res = await fetch("http://localhost:5000/chat", {
                    method: "POST",
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ message: input })
                });
                var temp = await res.json();
                setRecv([...recv, temp.message]);
            }
            //setArr([...arr, recv])
            setInput("");
        }

    }

    return (
        <div className={css.bdy}>
            <button onClick={() => setSlide(!slide)}><i className={`fa-solid  ${slide ? "" : "rotate-180"} transition ease-out delay-300 fa-circle-arrow-right fa-2xl ${css.slide}`} style={{ color: "#f7e22b" }}></i></button>
            <div className={css.top}>
                <h1><i class="fa-solid fa-robot fa-shake fa-lg"></i><span className='ml-2'>Krypto Bot</span></h1>
            </div>

            <div className={`${slide ? "max-lg:translate-x-[-300vw]" : ""} ${css.sidebar} transition ease-out delay-300`}>
                <PixelArtCard hover={false} random={true} size={200} tags={[(gen === "male") ? "human-male" : "human-female"]} />
                <h1 className="mb-12 text-xl mt-2">Hello, <span className='text-yellow-400 font-bold'>{name}</span>!</h1>

                <button onClick={() => { setActiv({ one: true, two: false, three: false }); setSlide(!slide) }} className={`h-[40px] w-[120px]  ${css.btn}`} style={{ backgroundImage: activ.one ? "var(--prim)" : "" }}>
                    FAQ</button>
                <button onClick={() => { setActiv({ one: false, two: true, three: false }); setSlide(!slide) }} className={`h-[40px] w-[120px] ${css.btn}`} style={{ backgroundImage: activ.two ? "var(--prim)" : "" }}>
                    Analytics</button>
                <button onClick={() => { setActiv({ one: false, two: false, three: true }); setSlide(!slide) }} className={`h-[40px] w-[120px] ${css.btn}`} style={{ backgroundImage: activ.three ? "var(--prim)" : "" }}>
                    Price</button>
            </div>

            <div className={css.chatArea}  >
                {
                    arr.map((data, i) => {
                        
                            <>
                                <div key={i} className={`${css.mssg1}`}>
                                    <p>{data}</p>
                                </div>
                                <div className={`${css.mssg2}`} ><p>{recv[i]}</p></div>
                            </>
                        
                    })
                }

                {/* for autoscroll */}
                <div ref={mssgend}></div>
            </div>

            <div className={css.foot}>
                <form onSubmit={send} className={css.inp}>
                    <input className={css.inpu} onChange={changeInput} value={input} placeholder='How can we help you today?'></input>
                    <button className={`h-[40px] w-[130px] ${css.btn}`} style={{ backgroundImage: "var(--prim)" }} type='submit'> <i className="fa-solid fa-paper-plane m-2"></i></button>
                </form>
            </div>
        </div>
    )
}

export default Chat
