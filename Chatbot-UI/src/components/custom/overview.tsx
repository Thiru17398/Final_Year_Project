import { motion } from 'framer-motion';
import { MessageCircle, BotIcon } from 'lucide-react';

export const Overview = () => {
  return (
    <>
    <motion.div
      key="overview"
      className="max-w-3xl mx-auto md:mt-20"
      initial={{ opacity: 0, scale: 0.98 }}
      animate={{ opacity: 1, scale: 1 }}
      exit={{ opacity: 0, scale: 0.98 }}
      transition={{ delay: 0.75 }}
    >
      <div className="rounded-xl p-6 flex flex-col gap-8 leading-relaxed text-center max-w-xl">
        <p className="flex flex-row justify-center gap-4 items-center">
          <BotIcon size={44}/>
          <span>+</span>
          <MessageCircle size={44}/>
        </p>
        <p>
          Welcome to <strong>Transit Simplified</strong><br />
          I am your <strong>Travel Guide</strong> <br/> you can ask me any <br/><strong>Transport Related Queries</strong>.
        </p>
      </div>
    </motion.div>
    </>
  );
};
