import { Button } from '@/components/ui/button';
import { Card } from "@/components/ui/card";

export default function Tournament() {
    return (

            <div className='border-white border-2 rounded-lg border-opacity-50 h-full flex p-4 justify-center items-center'>

                <div className='h-full w-1/3 space-y-2'>
                    <div className='h-1/2 w-full  p-2 space-y-2'>
                        <div className="w-full h-1/3 border rounded-lg border-opacity-45 p-2 bg-white bg-opacity-15 border-white mt-16">
                            <div className="w-full h-1/3 flex justify-center text-sm">Player 1</div>
                            <div className="w-full h-1/2 flex justify-center items-center">...</div>
                        </div>
                        <div className="w-full h-1/3 border rounded-lg border-opacity-45 bg-white bg-opacity-15 p-2 border-white">
                            <div className="w-full h-1/3 flex justify-center text-sm">Player 2</div>
                            <div className="w-full h-1/2 flex justify-center items-center">...</div>
                        </div>
                    </div>
                    <div className='h-1/2 w-full  p-2 space-y-2'>
                        <div className="w-full h-1/3 border rounded-lg border-opacity-45 bg-white bg-opacity-15 p-2 border-white mt-10">
                            <div className="w-full h-1/3 flex justify-center text-sm">Player 3</div>
                            <div className="w-full h-1/2 flex justify-center items-center">...</div>
                        </div>
                        <div className="w-full h-1/3 border rounded-lg border-opacity-45 bg-white bg-opacity-15 p-2 border-white">
                            <div className="w-full h-1/3 flex justify-center text-sm">Player 4</div>
                            <div className="w-full h-1/2 flex justify-center items-center">...</div>
                        </div>
                    </div>
                </div>

                <div className='  h-full w-1/3 flex justify-center items-center'>
                        <div className=' h-1/3 w-full p-4 space-y-2'>
                            <div className="w-full h-1/2 border rounded-lg border-opacity-45 bg-white bg-opacity-15 p-2 border-white">
                                <div className="w-full h-1/3 flex justify-center text-sm">Player 5</div>
                                <div className="w-full h-1/2 flex justify-center items-center">...</div>
                            </div>
                            <div className="w-full h-1/2 border rounded-lg border-opacity-45 bg-white bg-opacity-15 p-2 border-white">
                                <div className="w-full h-1/3 flex justify-center text-sm">Player 6</div>
                                <div className="w-full h-1/2 flex justify-center items-center">...</div>
                            </div>
                        </div>
                </div>

                <div className='  h-full w-1/3 flex justify-center items-center p-4'>
                    <div className='border rounded-lg border-opacity-45 bg-white bg-opacity-15 p-2 border-white h-1/6 w-full'>
                        <div className="w-full h-1/3 flex justify-center text-sm">Winner</div>
                        <div className="w-full h-1/2 flex justify-center items-center">...</div>
                    </div>
                </div>
                
            </div>
        

    );
}