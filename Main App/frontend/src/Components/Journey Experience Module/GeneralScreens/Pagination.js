import React from 'react'
import '../../../Styles/Pagination.css'
import { FaChevronLeft, FaChevronRight } from 'react-icons/fa'
import { TiMinus } from 'react-icons/ti'

const Pagination = ({ page , noOfPages, changePage }) => {
    

    function numberRange(start, end) {
        
        return new Array(parseInt(end) - parseInt(start)).fill().map((d, i) => i + start);
    }

    let middlePagination;

    if (noOfPages <= 5) {
        middlePagination = [...Array(noOfPages)].map((__, index) => (

            <button
                key={index + 1}
                onClick={() => changePage(index + 1)}
                disabled={page === index + 1}
            >
                {index + 1}

            </button>

        ))
    }
    else {
        const startValue = (Math.floor((page - 1) / 5) * 5);
        

        middlePagination = (
            <>
                {numberRange(startValue, noOfPages).map((__, index) => (
                    <button
                        key={startValue + index + 1}
                        onClick={() => changePage(startValue + index + 1)}
                        disabled={page === startValue + index + 1}
                    >
                        {startValue + index + 1}
                    </button>

                ))}
                <button>...</button>
                <button

                    onClick={() => changePage(noOfPages)} disabled={page === noOfPages}>
                    {noOfPages}
                </button>
            </>
        );

        if (page > 5) {
            if (noOfPages - page >= 5) {
                middlePagination = (
                    <>
                        <button onClick={() => changePage(1)}>1</button>
                        <button>...</button>
                        <button onClick={() => changePage(startValue)}>{startValue}</button>

                        {numberRange(startValue, noOfPages).map((__, index) => (
                            <button
                                key={startValue + index + 1}
                                onClick={() => changePage(startValue + index + 1)}

                                disabled={page === startValue + index + 1}

                            >
                                {startValue + index + 1}
                            </button>

                        ))}
                        <button>...</button>
                        <button
                            onClick={() => changePage(noOfPages)}>
                            {noOfPages}
                        </button>
                    </>
                )
            }

            else {
                let amountLeft = noOfPages - page + 5
                middlePagination = (
                    <>
                        <button onClick={() => changePage(1)}>1</button>
                        <button>...</button>
                        <button onClick={() => changePage(startValue)}>{startValue}</button>
                        {numberRange(amountLeft, noOfPages).map((__, index) => (
                            <button
                                key={startValue + index + 1}
                                onClick={() => changePage(startValue + index + 1)}

                                disabled={page === startValue + index + 1}

                                style={noOfPages < startValue + index + 1 ? { display: "none" } : null}
                            >
                                {startValue + index + 1}
                            </button>

                        ))}

                    </>
                )
            }
        }


    }



    return (

        noOfPages > 1 && (


            <div className="pagination">

                <button className='pagination__prev'
                    onClick={() => changePage(page - 1)}
                    disabled={page === 1}
                >
                    {page === 1 ? <TiMinus color='gray' /> :
                        <FaChevronLeft />

                    }

                </button>

                {middlePagination}


                <button className='pagination__next'
                    onClick={() => changePage(page + 1)}
                    disabled={page === noOfPages}
                >
                    {page === noOfPages ? <TiMinus color='gray' /> :
                        <FaChevronRight />

                    }
                </button>

            </div>

        )

    );
}

export default Pagination